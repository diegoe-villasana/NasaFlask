document.addEventListener('DOMContentLoaded', function() {
    const carouselSlide = document.querySelector('.carousel-slide');
    if (carouselSlide) {
        const images = document.querySelectorAll('.carousel-slide img');
        if (images.length === 0) return;

        let counter = 0;
        const numImages = images.length;
        
        function slide() {
            counter++;
            if (counter >= numImages) {
                counter = 0;
            }
            const offset = -counter * (100 / numImages);
            carouselSlide.style.transform = `translateX(${offset}%)`;
        }

        // Ajustar el ancho del slide dinámicamente
        carouselSlide.style.width = `${numImages * 100}%`;
        images.forEach(img => {
            img.style.width = `${100 / numImages}%`;
        });

        setInterval(slide, 4000); // Cambia la imagen cada 4 segundos
    }
});