import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import google

#Later add the send mail fn
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices) [<pyttsx3.voice.Voice object at 0x000001C6A4443400>, <pyttsx3.voice.Voice object at 02x000001C6A4443370>]
engine.setProperty('voice',voices[1].id) #Using 2nd voice
#print(voices[0].id) HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
#print(voices[1].id) HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

'''def sendEmail(to,content):
	#Firstly you have to allow gmail access to less secure apps. Steps are in the following link
	#https://hotter.io/docs/email-accounts/secure-app-gmail/
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login("Enter your mail ID","Enter your password") #Type your password or import it from other text file ,or use some different mechanism
	server.sendmail("Enter your mail ID",to,content)
	server.close()'''

def speak(audio):
	engine.say(audio)
	engine.runAndWait() #Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately. Returns when all commands queued before this call are emptied from the queue.

def wish(): #It wishes you
	hour=int(datetime.datetime.now().hour) 
	if hour>=6 and hour<12:
		speak("Good Morning Shreyas")
	elif hour>=12 and hour<17:
		speak("Good afternoon Shreyas")
	elif hour>=17 and hour<=22:
		speak("Good Evening Shreyas")
	else:
		speak("Welcome Shreyas")
	speak("I'm Alexa. How may I help you")

def my_files(query):
	if "c drive" in query:
		loc="C:"
	elif "d drive" in query:
		loc="D:"
	elif "e drive" in query:
		loc="E:"
	elif "f drive" in query:
		loc="F:"
	print(os.listdir(loc))
	return loc


def takecommand(): #It takes microphone input from the user and returns string output
	r=sr.Recognizer() #Recognizes the voice from voice input device
	with sr.Microphone() as source: # use the default microphone as the audio source
		print("Listening...")
		r.pause_threshold=1 #It provides time for the speaker to complete the orders
		audio=r.listen(source)
	
	try:
		print("Recognizing...")
		query=r.recognize_google(audio,language='en-in') 
		print(f"User said: {query}\n")
	
	except Exception as e: #If it can't listen anything
		#print(e) It prints the exception error
		print("Sorry, sir can you repeat it please")
		speak("Sorry, sir can you repeat it please")
		return "None"
	return query


if __name__ == '__main__':
	wish()
	while(True):
		query=takecommand().lower()
		#Logic to execute tasks based on query
		
		if "wikipedia" in query:
			speak("Searching Wikipedia...")
			query=query.replace("Wikipedia","")
			results=wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			print(results)
			speak(results)

		elif "my files" in query:
			query=query.replace("my files","")
			loc=my_files(query)

			#print(query)

		elif "folder" in query:
			query=query.replace("folder","")
			loc=loc+"\\"+query
			print("Select the desired directory")
			print(os.listdir(loc))
			
		elif "open file" in query:
			os.startfile(loc)
		
		elif "exit" in query:
			exit()

		elif "google search" in query:
			speak("Searching on google...")
			query=query.replace("google search","")
			webbrowser.get(chrome_path).open('http://www.google.com/search?q='+str(query))

		elif "open youtube" in query:
			webbrowser.get(chrome_path).open('youtube.com')

		elif "youtube search" in query:
			query=query.replace("youtube serch","")
			webbrowser.get(chrome_path).open('https://www.youtube.com/results?search_query='+query)

		elif "open google" in query:
			webbrowser.get(chrome_path).open('google.com')

		elif "listen songs" in query:
			webbrowser.get(chrome_path).open('open.spotify.com')

		elif "play song" in query:
			query=query.replace("play song","")
			webbrowser.get(chrome_path).open('https://open.spotify.com/search/'+query)

		elif "open mail" in query:
			webbrowser.get(chrome_path).open('mail.google.com')

		elif "open meet" in query:
			webbrowser.get(chrome_path).open('meet.google.com')

		elif "open classroom" in query:
			webbrowser.get(chrome_path).open('classroom.google.com')

		elif "open drive" in query:
			webbrowser.get(chrome_path).open('drive.google.com')

		elif "stackoverflow" in query:
			webbrowser.get(chrome_path).open('stackoverflow.com')

		elif "github" in query:
			webbrowser.get(chrome_path).open('github.com')

		elif "coursera" in query:
			webbrowser.get(chrome_path).open('coursera.org')

		elif "linkedin" in query:
			webbrowser.get(chrome_path).open('linkedin.com')

		elif "animixplay" in query:
			webbrowser.get(chrome_path).open('animixplay.to')

		elif "send email" in query:
			try:
				speak("What should I send")
				#print("What should I send?")
				content=takecommand()
				to="Enter Reciever's mail ID"
				sendEmail(to,content)
				speak("Email sent")
				print("Email sent")
			except Exceptionas as e:
				#print(e)
				speak("Sorry email has not been sent")
				#print("Sorry! Email has not been sent")

		elif "scam" in query:
			scam_1992_dir="F:\\Scam 1992 - The Harshad Mehta Story (2020) S01 Hindi (1080p WEBRip x265 10bit) - [Musafirboy]"
			episodes=os.listdir(scam_1992_dir)
			#print(episodes)
			if "episode 1" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[0]))
			elif "episode 2" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[1]))
			elif "episode 3" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[2]))
			elif "episode 4" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[3]))
			elif "episode 5" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[4]))
			elif "episode 6" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[5]))
			elif "episode 7" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[6]))
			elif "episode 8" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[7]))
			elif "episode 9" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[8]))
			elif "episode 10" in query:
				os.startfile(os.path.join(scam_1992_dir,episodes[9]))

		elif "stranger things" in query:
			stranger_things_dir="F:\\Stranger Things Season 2 Mp4 1080p"
			episodes=os.listdir(stranger_things_dir)
			#print(episodes)
			if "episode 1" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[0]))
			elif "episode 2" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[1]))
			elif "episode 3" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[2]))
			elif "episode 4" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[3]))
			elif "episode 5" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[4]))
			elif "episode 6" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[5]))
			elif "episode 7" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[6]))
			elif "episode 8" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[7]))
			elif "episode 9" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[8]))
			elif "episode 10" in query:
				os.startfile(os.path.join(stranger_things_dir,episodes[9]))


#pyinstaller  --onefile --hidden-import=pyttsx3.drivers Desktop_Assistance.py
#This must be done to create .exe file