# text to speech conversion
from gtts import gTTS
import os

mytext = "Thank you for watching our demonstration!"
language = 'en'

my_obj = gTTS(text=mytext, lang=language, slow=False)

my_obj.save("bd_previse_23.mp3")
os.system("female_db_previse/bd_previse_23.mp3")