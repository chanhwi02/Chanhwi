from gtts import gTTS
import playsound

tts = gTTS("Hi, goot to see u", lang='en')
tts.save("news_Son.mp3")
playsound.playsound("news_Son.mp3",True)
