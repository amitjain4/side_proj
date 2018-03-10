from googlesearch.googlesearch import GoogleSearch
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	audio = r.listen(source)
#question = raw_input("Enter all question ")
#option = raw_input("enter options ")
	print r.recognize_google(audio)

response = GoogleSearch().search(r.recognize_google(audio))
for result in response.results:

    print("Title: " + result.title)
    print("Content: " + result.getText())
