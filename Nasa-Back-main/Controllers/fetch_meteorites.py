import math
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)


def impacto_meteorito(diametro, velocidad, densidad):
    volumen = (4/3) * math.pi * ((diametro/2)**3)  # km³
    masa = densidad * volumen
    velocidad = velocidad * 1000  # km/s -> m/s
    energia_cinetica = 0.5 * masa * (velocidad**2)  # Joules
    # Conversión a megatones TNT
    tnt = energia_cinetica / 4.184e9 
    tnt /= 1_000_000
    return round(tnt, 3)

def calcular_diametro_crater(tnt):#diamertrooo
    c = 0.15
    b = 1/3.5
    crater_diameter = c * tnt**b
    return round(crater_diameter, 3)

def terremotos_meteorito(tnt):
    if tnt < 1:
        magnitude = 1.0
    else:
        magnitude = 1 + (2/3) * math.log10(tnt)
    return round(magnitude, 2)

def distancia_onda(energy_megatons):
    k = 6  # constante empírica
    return round(k * energy_megatons ** (1/3), 2)



def ciudades_cercanas(lat, lon, radio_km):#traer las ciudades
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    resp = requests.get(url, headers={"User-Agent": "MiAppMeteoritos"})
    print("Nominatim response:", resp.text)
    if resp.status_code == 200:
        data = resp.json()
        ciudad = data.get("address", {}).get("city")
        if ciudad:
            return [{"city": ciudad, "lat": data.get("lat"), "lon": data.get("lon") }]
        else:
            return []
    else:
        return []



@app.route("/calcular_crater", methods=["POST"])
def calcular_crater():
    data = request.get_json()
    try:
        diametro = float(data["diametro"])   # km
        velocidad = float(data["velocidad"]) # km/s
        densidad = float(data["densidad"])   # kg/m³
        lon = float(data["longitud"]) 
        lat = float(data["latitud"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Parámetros inválidos. Envía 'diametro', 'velocidad', 'densidad', 'latitud', 'longitud'"}), 400


    energy_megatons = impacto_meteorito(diametro, velocidad, densidad)
    crater_diameter = calcular_diametro_crater(energy_megatons)
    onda_expansiva = distancia_onda(energy_megatons)
    magnitud_sismo = terremotos_meteorito(energy_megatons)

    # Ciudades
    ciudades_destruidas = ciudades_cercanas(lat, lon, crater_diameter/2)
    ciudades_onda = ciudades_cercanas(lat, lon, onda_expansiva)

    # Filtrar ciudades que reciben la onda expansiva pero no están dentro del cráter
    ids_destruidas = {c["city"] for c in ciudades_destruidas}
    ciudades_afectadas = [c for c in ciudades_onda if c.get("city") not in ids_destruidas]


    resultado = {
        "energia_megatones": energy_megatons,
        "diametro_crater_km": crater_diameter,
        "onda_expansiva_km": onda_expansiva,
        "magnitud_sismo": magnitud_sismo,
        "ciudades_destruidas": ciudades_destruidas,
        "ciudades_afectadas": ciudades_afectadas
    }

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)

