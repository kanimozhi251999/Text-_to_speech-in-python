#Convert Text into Speech

#Import gTTS library and “os” module in order to play the converted audio
from gtts import gTTS 
import os
C#reating a text that we want to convert into audio
text = 'Global warming is the long-term rise in the average temperature of the Earth’s climate system'
#gTTS supports multiple languages. Please refer to the documentation here. Selected ‘en’ -> English and stored in the language variable
language = 'en'
#Creating an object called speech and passing the text and language to the engine. Marked slow = False which tells the module that the converted audio should have a high speed.
speech = gTTS(text = text, lang = language, slow = False)
#Saving the converted audio in a mp3 file named called ‘text.mp3’
speech.save('text.mp3')
#Playing the converted file, using Windows command ‘start’ followed by the name of the mp3 file.
os.system('start text.mp3')
