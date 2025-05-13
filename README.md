# 🤖 EmpleaBot – Asistente Virtual para Empleados

EmpleaBot es un chatbot de Telegram diseñado para actuar como un asistente emocional y funcional para empleados de una empresa en Argentina. Utiliza el modelo de lenguaje **Gemini (Google Generative AI)** para generar respuestas naturales dentro de un contexto laboral.

---

## 🚀 Características

- Conectado a **Telegram** mediante `python-telegram-bot`.
- Alimentado por **Gemini 2.0 Flash** para respuestas generativas.
- Reconocimiento de **saludos y despedidas**.
- Detección de **temas prohibidos** (como política).
- Historial conversacional para mantener coherencia.
- Diseño enfocado en el **apoyo emocional de empleados**.

---

## ⚙️ Requisitos

- Python 3.8+
- Claves API de:
  - [Google Generative AI (Gemini)](https://makersuite.google.com/)
  - Bot de Telegram ([crear desde @BotFather](https://t.me/BotFather))

## Instalación de dependencias

```bash
pip install python-telegram-bot google-generativeai
```

##🧠 Lógica del Bot

    Responde saludos amigablemente, sin repetir si ya se dio uno.

    Evita hablar de política u otros temas sensibles.

    Apoya emocionalmente a los empleados, detectando emociones implícitas en el mensaje.

    Responde solo temas laborales, evitando desvíos innecesarios.

##🏃 Ejecución

python nombre_del_script.py

📂 Estructura del Código

    start(update, context) → Maneja el comando /start.

    handle_message(update, context) → Procesa cada mensaje textual.

    obtener_respuesta(mensaje_usuario) → Genera la respuesta usando Gemini.

    main() → Configura el bot y lo pone en marcha con polling.

##🛑 Temas Prohibidos

Estos temas no se responden y generan un aviso:

["política", "presidente", "elecciones", "gobierno", "partido", "ideología", "congreso"]

##🧑‍💼 Casos de Uso

    Asistencia emocional para empleados.

    Consulta sobre temas internos de la empresa.

    Soporte fuera del horario laboral.

##📌 Notas

    El bot guarda un historial limitado (últimos 10 mensajes) para mantener el contexto.

    Diseñado para entornos corporativos o pruebas de IA en RRHH.

    Ideal para proyectos educativos o de prototipo.
