# text to speech conversion
from gtts import gTTS
import os

# The text that you want to convert to audio
mytext = "Привет, Георги! Поздрави от Виолета!"

# Language in which you want to convert
language = 'bg'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("greetings.avi")

os.system("greetings.avi")