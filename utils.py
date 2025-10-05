# app/utils.py

import math

def calculate_impact_energy(diameter, velocity, density):
    """Calcula la energía cinética de un asteroide en megatones de TNT."""
    if diameter <= 0 or velocity <= 0 or density <= 0:
        return 0

    mass = (4/3) * math.pi * (diameter / 2)**3 * density
    # Convertir velocidad de km/s a m/s
    velocity_ms = velocity * 1000
    kinetic_energy_joules = 0.5 * mass * (velocity_ms ** 2)

    # Convertir Joules a megatones de TNT (1 megatón = 4.184e15 Joules)
    return kinetic_energy_joules / 4.184e15

def calculate_crater_diameter(energy_megatons):
    """Estima el diámetro del cráter de impacto en metros."""
    if energy_megatons <= 0:
        return 0

    # Convertir energía a Joules para la fórmula
    energy_joules = energy_megatons * 4.184e15

    # Ley de escala simplificada para roca sedimentaria
    # D = 1.161 * (rho_t / g)^(-0.22) * W^(0.294) - esta es más compleja
    # Usaremos una aproximación más simple
    crater_diameter_meters = 1.8 * (energy_joules / 1800)**(1/3.4) * 1.25 # Coeficiente para roca y ajuste final

    return crater_diameter_meters