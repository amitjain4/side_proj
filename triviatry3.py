import time
import keyboard
import speech_recognition as sr


# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
    

r = sr.Recognizer()
m = sr.Microphone()

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening
while True:
    try:
        if keyboard.is_pressed(' '):
            stop_listening(wait_for_stop=False)
            print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
            print('Done Voice Input')
            break
            
    except:
        pass
# calling this function requests that the background listener stop listening


##callback is like a function run like a thread which can asynchronously provide data
