const API_URL = "http://localhost:8000/estudiantes"
const btn_guardar = document.getElementById("btn_guardar")
const formulario = document.getElementById("formulario")

btn_guardar.onclick = async (event) => {
    event.preventDefault();
    const estudiante = {
        matricula: document.getElementById("matricula").value,
        nombre: document.getElementById("nombre").value,
        apellidos: document.getElementById("apellidos").value,
        genero: document.getElementById("genero").value,
        direccion: document.getElementById("direccion").value,
        telefono: document.getElementById("telefono").value
    };
    console.log(estudiante)
    // REQUEST -> solicitud enviar datos (Generalmente desde el front)
    // RESPONSE -> Respuesta obtener datos (Gneralmente desde el back)
    await fetch(
        API_URL, 
        {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(estudiante)
        }
    ).then(response => response.json())
    .then(response => console.log(response))
    .catch(err => console.error(err));
    formulario.reset();
}
function alert_hola_mundo() {
    document.getElementById("parrafo").innerHTML = "HOLA MUNDO";
    alert("hola mundo");
}

