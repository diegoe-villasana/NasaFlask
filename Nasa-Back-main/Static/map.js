document.addEventListener('DOMContentLoaded', function () {
    // Inicializar el mapa y centrarlo en una vista global
    var map = L.map('map').setView([20, 0], 2);

    // Añadir la capa base de OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    let impactMarker;
    let impactCircle;

    // Evento de clic en el mapa para colocar el marcador de impacto
    map.on('click', function(e) {
        // Si ya existe un marcador, lo elimina
        if (impactMarker) {
            map.removeLayer(impactMarker);
        }
        // Añade un nuevo marcador en la ubicación del clic
        impactMarker = L.marker(e.latlng).addTo(map)
            .bindPopup('Punto de impacto seleccionado.')
            .openPopup();
    });

    // Evento de envío del formulario
    document.getElementById('impact-form').addEventListener('submit', function(e) {
        e.preventDefault(); // Evita que la página se recargue

        if (!impactMarker) {
            alert('Por favor, selecciona un punto de impacto en el mapa haciendo clic en él.');
            return;
        }

        // Obtener los valores del formulario
        const diameter = parseFloat(document.getElementById('diameter').value);
        
        // Estimación simple del radio del cráter (ej: 10 veces el diámetro del proyectil)
        const craterRadius = diameter * 10;

        // Si ya existe un círculo, lo elimina
        if (impactCircle) {
            map.removeLayer(impactCircle);
        }

        // Dibuja un nuevo círculo en la ubicación del marcador
        impactCircle = L.circle(impactMarker.getLatLng(), {
            radius: craterRadius,
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5
        }).addTo(map);

        // Ajusta la vista del mapa para mostrar el cráter completo
        map.fitBounds(impactCircle.getBounds());
    });
});
