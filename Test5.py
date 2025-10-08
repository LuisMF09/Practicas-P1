import PyPDF2
import pyttsx3

# Abrir el PDF
path = open("cuento_prueba.pdf", "rb")
pdfReader = PyPDF2.PdfReader(path)

# Inicializar el motor de voz
speak = pyttsx3.init()

# Recorrer todas las páginas
for page in pdfReader.pages:
    text = page.extract_text()
    if text:  # Para evitar errores si alguna página está vacía
        speak.say(text)
        speak.runAndWait()

speak.stop()
