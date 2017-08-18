#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os

def speak():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        userSpeech = r.recognize_google(audio)
        if(userSpeech == 'open Steam'):
            os.system(r'"C:\Program Files (x86)\Steam\Steam.exe"')
            speak()

        if(userSpeech == 'open Chrome'):
            os.system(r'"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
            speak()

        if(userSpeech == 'open Spotify'):
            os.system(r'"C:\Users\Master\AppData\Roaming\Spotify\Spotify.exe"')
            speak()
            
        if(userSpeech == 'close'):
            quit()
            
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    speak()


if __name__ == "__main__":
    speak()
