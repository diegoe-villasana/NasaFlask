

async function mas_desasttrosos() {
    try {
        const response = await fetch("http://127.0.0.1:5000/lista");
        if (response.ok) {
            const data = await response.json();
            console.log(data);
        } else {
            console.error("Retorno no exitoso, código:", response.status);
        }
    } catch (error) {
        console.error("Error al hacer fetch:", error);
    }
}

window.addEventListener("DOMContentLoaded", mas_desasttrosos);


