import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------------

st.set_page_config(
    page_title="Compabot",
    page_icon="🤖",
    layout="centered"
)

# ---------------------------------------------------------
# PERSONALIDAD DEL CHATBOT
# ---------------------------------------------------------

PERSONALIDAD = """
Eres Compabot, un chatbot creado como proyecto académico.

Tu personalidad es una combinación de las características,
gustos y preferencias de cinco estudiantes entrevistados.

Eres amigable, creativo, responsable, colaborativo y positivo.

Te gustan temas como:
- Música
- Películas
- Deportes
- Comida
- Programación
- Matemáticas
- Inglés
- Biología
- Física

Debes responder de forma sencilla, amable y cercana.
"""

# ---------------------------------------------------------
# RESPUESTAS DEL CHATBOT
# ---------------------------------------------------------

def generar_respuesta(mensaje):

    mensaje = mensaje.lower()

    if "hola" in mensaje or "buenas" in mensaje:
        return (
            "¡Hola! Soy Compabot 🤖. "
            "Fui creado a partir de la información obtenida "
            "de cinco estudiantes. ¿Sobre qué quieres hablar?"
        )

    elif "quién eres" in mensaje or "quien eres" in mensaje:
        return (
            "Soy Compabot, un chatbot académico cuya personalidad "
            "combina los gustos y características de cinco estudiantes."
        )

    elif "música" in mensaje or "musica" in mensaje:
        return (
            "Mi personalidad combina diferentes gustos musicales, "
            "como reguetón, pop, rap y rock."
        )

    elif "película" in mensaje or "pelicula" in mensaje:
        return (
            "Entre las películas relacionadas con los gustos de los "
            "estudiantes están Spider-Man, Barbie, Avengers, "
            "Enola Holmes e Interestelar."
        )

    elif "deporte" in mensaje:
        return (
            "Me gustan diferentes deportes, entre ellos fútbol, "
            "voleibol, natación y baloncesto."
        )

    elif "comida" in mensaje:
        return (
            "Algunos de los platos favoritos de los estudiantes "
            "son pizza, pasta, hamburguesa, sushi y pollo."
        )

    elif "materia" in mensaje:
        return (
            "Las materias favoritas representadas en mi personalidad "
            "son matemáticas, inglés, programación, biología y física."
        )

    elif "fortaleza" in mensaje:
        return (
            "Entre mis fortalezas están la responsabilidad, "
            "creatividad, liderazgo, organización y trabajo en equipo."
        )

    elif "debilidad" in mensaje:
        return (
            "Algunas debilidades presentes en la información de los "
            "estudiantes son timidez, nervios, impaciencia, "
            "distracción y desorden."
        )

    elif "programación" in mensaje or "programacion" in mensaje:
        return (
            "La programación es uno de los temas que más me interesa. "
            "Con ella puedo trabajar con datos, aplicaciones y sistemas."
        )

    elif "gracias" in mensaje:
        return (
            "¡Con mucho gusto! Me alegra poder ayudarte. 🤖"
        )

    elif "adiós" in mensaje or "adios" in mensaje:
        return (
            "¡Hasta luego! Espero que hayas disfrutado hablando conmigo."
        )

    else:
        return (
            "Es un tema interesante. Recuerda que mi personalidad "
            "se construyó combinando la información obtenida de "
            "cinco estudiantes. Puedes preguntarme sobre música, "
            "películas, deportes, comida, materias, fortalezas "
            "o debilidades."
        )


# ---------------------------------------------------------
# TÍTULO
# ---------------------------------------------------------

st.title("🤖 Compabot")

st.subheader("Chatbot de voz basado en la personalidad de cinco estudiantes")

st.write(
    "Este chatbot fue desarrollado como parte de la Actividad 6 "
    "de bases de datos. Su personalidad combina información "
    "obtenida mediante entrevistas."
)

# ---------------------------------------------------------
# INFORMACIÓN
# ---------------------------------------------------------

with st.expander("ℹ️ Sobre Compabot"):

    st.write(PERSONALIDAD)

# ---------------------------------------------------------
# HISTORIAL DEL CHAT
# ---------------------------------------------------------

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes anteriores

for mensaje in st.session_state.mensajes:

    with st.chat_message(mensaje["rol"]):

        st.write(mensaje["contenido"])

# ---------------------------------------------------------
# ENTRADA DEL USUARIO
# ---------------------------------------------------------

pregunta = st.chat_input(
    "Escribe tu pregunta..."
)

# ---------------------------------------------------------
# PROCESAMIENTO DEL MENSAJE
# ---------------------------------------------------------

if pregunta:

    # Guardar mensaje del usuario
    st.session_state.mensajes.append(
        {
            "rol": "user",
            "contenido": pregunta
        }
    )

    # Generar respuesta
    respuesta = generar_respuesta(pregunta)

    # Guardar respuesta
    st.session_state.mensajes.append(
        {
            "rol": "assistant",
            "contenido": respuesta
        }
    )

    # Actualizar pantalla
    st.rerun()

# ---------------------------------------------------------
# BOTÓN PARA LIMPIAR EL CHAT
# ---------------------------------------------------------

if st.button("🗑️ Limpiar conversación"):

    st.session_state.mensajes = []

    st.rerun()

# ---------------------------------------------------------
# FUNCIÓN DE VOZ
# ---------------------------------------------------------

st.divider()

st.subheader("🔊 Respuesta por voz")

st.write(
    "Después de recibir una respuesta, puedes utilizar "
    "la función de lectura de voz de tu navegador para escucharla."
)

if st.session_state.mensajes:

    ultima_respuesta = None

    for mensaje in reversed(st.session_state.mensajes):

        if mensaje["rol"] == "assistant":

            ultima_respuesta = mensaje["contenido"]

            break

    if ultima_respuesta:

        # JavaScript para leer la respuesta
        texto_voz = ultima_respuesta.replace("'", "\\'")

        html_voz = f"""
        <script>
        function hablar() {{
            let texto = '{texto_voz}';

            let mensaje = new SpeechSynthesisUtterance(texto);

            mensaje.lang = 'es-ES';
            mensaje.rate = 1;
            mensaje.pitch = 1;

            window.speechSynthesis.speak(mensaje);
        }}
        </script>

        <button onclick="hablar()"
        style="
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        ">
        🔊 Escuchar respuesta
        </button>
        """

        st.components.v1.html(
            html_voz,
            height=60
        )

# ---------------------------------------------------------
# PIE DE PÁGINA
# ---------------------------------------------------------

st.divider()

st.caption(
    "Proyecto académico - Actividad 6 - Desarrollo de Bases de Datos"
)
