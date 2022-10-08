# text to speech conversion
from gtts import gTTS
import os

# The text that you want to convert to audio
mytext = "Привет, Вили! Поздрави и целувки от Галя"

# Language in which you want to convert
language = 'bg'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("greetings.mp3")

os.system("greetings.mp3")
