import pyttsx3
text_speech = pyttsx3.init()

string = "This is an interface demonstration of a price index transfer from an MSSQL Database to ETRM System Previse Coral."

text_speech.say(string)
text_speech.save_to_file(string, 'speech.mp3')
text_speech.runAndWait()