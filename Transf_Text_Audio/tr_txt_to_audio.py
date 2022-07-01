from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'
audio2 = 'audio2.mp3'
language1 = 'pt-br'
sp = gTTS(
    text='Você deve ter cautela ao executar aplicativos sem saber do que se trata. Consegui lhe enganar. Foi instalado um keylogger em seu sistema. Suas credenciais estão expostas! O que você digitar, eu vou saber, isso em tempo real. A segurança do seu dispositivo foi violada!',
    lang=language
)

sp.save(audio)
playsound(audio)


