import pyttsx3

string = "This is an interface demonstration of a price index transfer from an MSSQL Database to ETRM System Previse " \
         "Coral. Automated data import is achieved with the standalone Enterprise Middleware called Universal Loader."

engine = pyttsx3.init()

# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'speech.mp3')

engine.runAndWait()