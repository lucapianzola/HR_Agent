import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
# Configurar Gemini con tu clave de API
genai.configure(api_key="TU_API_KEY")

# Crear el modelo de Gemini
model = genai.GenerativeModel("gemini-2.0-flash")

# Lista de saludos que activan una respuesta específica
saludos = ["hola", "buenas tardes", "buenas noches", "buenos días", "hey", "qué tal"]

# Lista de saludos de despedida que activan una respuesta específica
despedidas = ["chau", "adiós", "hasta luego", "nos vemos", "bye"]

# Lista de temas prohibidas
temas_prohibidos = ["política", "presidente", "elecciones", "gobierno", "partido", "ideología", "congreso"]

# Historial de mensajes
historial = []


def obtener_respuesta(mensaje_usuario):
    global historial

    historial.append({"role": "user", "content": mensaje_usuario})
    contexto = "\n".join([f"{m['role']}: {m['content']}" for m in historial[-10:]])

    # Crear contexto con estilo de diálogo
    mensaje = (
        f"Eres un asistente virtual de empleados de una empresa en Argentina."
        "Respondes de manera natural y sin repetir saludos si ya han sido mencionados."
        "Solo puedes responder cosas sobre trabajo, sobre empleados y sus emociones."
        "Las personas pueden expresar emociones, debes apoyarlas."
        "Aquí está la conversación hasta ahora:\n"
        f"{contexto}\n"
    )

    # Generación de respuesta usando el modelo Gemini
    respuesta = model.generate_content(mensaje)
    historial.append({"role": "assistant", "content": respuesta.text})
    return respuesta.text

# Función para manejar el comando '/start'
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy EmpleaBot. ¿En qué puedo ayudarte hoy?")

# Función para manejar los mensajes del usuario
async def handle_message(update: Update, context: CallbackContext):
    mensaje_usuario = update.message.text.strip().lower()

    # Verificar si el usuario quiere salir
    if mensaje_usuario in despedidas:
        await update.message.reply_text("¡Hasta luego! Que tengas un gran día.")
        return

    # Verificar si el mensaje contiene temas prohibidos
    if any(palabra in mensaje_usuario for palabra in temas_prohibidos):
        await update.message.reply_text("Lo siento, pero no puedo hablar de política. ¿Te puedo ayudar con otra cosa?")
        return

    # Verificar si el mensaje es un saludo
    if mensaje_usuario in saludos:
        await update.message.reply_text("¡Hola, Bienvenido! ¿En qué puedo ayudarte?")
        return

    # Generación de respuesta usando Gemini
    respuesta_bot = obtener_respuesta(mensaje_usuario)
    await update.message.reply_text(respuesta_bot)

# Función principal para configurar y ejecutar el bot de Telegram
def main():
    # Crear el objeto Application con el token de tu bot
    application = Application.builder().token("TU_TOKEN_TELEGRAM").build()

    # Manejar el comando '/start'
    application.add_handler(CommandHandler("start", start))

    # Manejar los mensajes de los usuarios
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot Corriendo...")

    # Iniciar el bot
    application.run_polling()
    
if __name__ == '__main__':
    main()
