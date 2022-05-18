from gtts import gTTS
from playsound import playsound
def getAudio(texto, nombre,idioma):
    s = gTTS(texto , lang= idioma) 
    s.save(nombre)
    playsound(nombre)

