import speech_recognition as sr # recognise speech
import webbrowser
import time
import playsound # to play an audio file
import os # to remove created audio files
import random
from gtts import gTTS # google text to speech
from time import ctime # get time details

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r=sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            laura_speak(ask)
        audio=r.listen(source) # listen for the audio via source
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError: # error: recognizer does not understand
            laura_speak('Sorry i didnt get what you saying')
        except sr.RequestError: # error: recognizer is not connected
            laura_speak('Sorry the service is down')
        return voice_data

def laura_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en') # creating the text to speach variable
    r=random.randint(1,10000000) #creating a randon string
    audio_file='audio-' + str(r) + '.mp3' # creationg the name of the audio file
    tts.save(audio_file) #save audio file as mp3
    playsound.playsound(audio_file) #play the audio file
    print(audio_string) # printing what app says
    os.remove(audio_file) # removing the audio file

def respond(voice_data):
    # name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if user.name:
            laura_speak("my name is Laura")
        else:
            laura_speak("my name is Laura.what's your name")


    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        laura_speak("okay i will remember that "+ person_name + ' nice to meet you')
        user.setName(person_name) # remember name in person object

    # app builder
    if there_exists(['who is your father']):
        laura_speak('My father is Mendel')
    
    # greeting
    if there_exists(["how are you","how are you doing"]):
        laura_speak("I'm very well, thanks for asking "+ user.name)

    # time 
    if there_exists(["what's the time","tell me the time","what time is it"]):
        laura_speak(ctime())

    # search
    if there_exists(["Google","search"]):
        search=record_audio('What do you want to search for on Google?')
        url = 'https://google.com/search?q='+ search
        webbrowser.get().open(url)
        laura_speak('Here is what i found for ' + search + ' on google')
    
    # youtube
    if there_exists(["YouTube"]):
        search=record_audio('What do you want to search for in youtube?')
        url = 'https://www.youtube.com/results?search_query='+search
        webbrowser.get().open(url)
        laura_speak('Here is what I found for ' + search +' on youtube')


    if there_exists(["location","find location","find a location","find my location"]):
        location=record_audio('What is the location')
        url = 'https://google.nl/maps/place/'+location+ '/&amp'
        webbrowser.get().open(url)
        laura_speak('Here is the location of ' + location)

    if there_exists(["exit"]):
        exit()

    

time.sleep(0.5)
laura_speak('How can i help you?')
user=person()
while 1:
    voice_data=record_audio()
    respond(voice_data)