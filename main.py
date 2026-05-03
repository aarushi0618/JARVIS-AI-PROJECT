import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import requests
import musicLibrary
from openai import OpenAI


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="1a3687176a084cc8af55869e9015cde1"
url=f"https://newsapi.org/v2/top-headlines?country=us&apiKey=1a3687176a084cc8af55869e9015cde1"
def speak(text):
  engine.say(text)
  engine.runAndWait()
def openai(c):
  client = OpenAI(
  api_key="YOUR_OPENAI_API_KEY_HERE"
  
  )

# Create the request (Python syntax)
  response = client.chat.completions.create(
  model="gpt-3.5-turbo", # Note: gpt-5-nano does not exist yet
  messages=
    {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
  
   )
  print(response.choices[0].message.content)
def processcommand(c):
  if "open google" in c.lower:
    webbrowser.open("https://google.com")
  elif "open facebook" in c.lower:
    webbrowser.open("https://facebook.com")
  elif "open youtube" in c.lower:
    webbrowser.open("https://youtube.com")
  elif "open linkedin" in c.lower:
    webbrowser.open("https://linkedin.com")
  elif c.lower().startswith("play"):
    song=c.lower().split(" ")[1]
    link=musicLibrary.music[song]
    webbrowser.open(link)
  elif "news" in c.lower():
    r=requests.get("url")

    if r.status_code==200:
      data=r.json() #parse the json response
      articles= data.get("articles",[]) #extract the articles
      for article in articles:
        speak(article['title'])
  else:
    #let opnAI handle the rest requests 
    output=openai(command)
    speak=output

  
    


 

if __name__=="__main__":
  speak("Initializing Jarvis")
  # Listen for the wake word "Jarvis"
  while True:
    # obtain audio from the microphone
     r = sr.Recognizer()
     
   

     

     # recognize speech using Sphinx
     try:
         with sr.Microphone() as source:
          
         
        # If your room is noisy, the recognizer might struggle to find the "start" of your phrase. You can add this line right before your with sr.Microphone() block to help the library calibrate:
       
          print("Listening!")
          
          audio = r.listen(source,timeout=5,phrase_time_limit=30)
          
          word=r.recognize_google(audio)
          if(word.lower()=="jarvis"):
             speak("ya")

             with sr.Microphone() as source:
         
        # If your room is noisy, the recognizer might struggle to find the "start" of your phrase. You can add this line right before your with sr.Microphone() block to help the library calibrate:
       
              print("Jarvis Active")
          
             audio = r.listen(source,timeout=2,phrase_time_limit=30)
             print("Recognizing")
             command=r.recognize_google(audio)
             processcommand(command)
            
     except sr.WaitTimeoutError:
      print("No speech detected within the timeout period.")
     except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
     except sr.RequestError as e:
          print(f"Could not request results from Google Speech Recognition service; {e}")
 