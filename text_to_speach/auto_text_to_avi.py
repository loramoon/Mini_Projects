import pyttsx3

text_speech = pyttsx3.init()
text_speech.setProperty('rate', 150)

file = open('subs.txt')
line_number = 0

while True:
    line = file.readline()
    if not line:
        break
    line_number += 1
    text_speech.say(line)
    file_name = str(line_number)+'_speech.avi'
    text_speech.save_to_file(line, file_name)
    text_speech.runAndWait()
file.close()