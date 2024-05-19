# assistant/views.py
from django.shortcuts import render, redirect
from .models import RememberedMessage
from .forms import RememberMessageForm
from gtts import gTTS
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
import os
import webbrowser
import pygame
import io
import threading
import time

# Function to speak out the provided text using gTTS
def talk(text):
    # Generate the TTS audio in memory
    tts = gTTS(text=text, lang='en')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # Initialize pygame mixer and load the audio from memory
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp, 'mp3')
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        continue

# Function to recognize speech input
def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print('Command:', command)
            return command
    except sr.UnknownValueError:
        # Exception handling for unintelligible speech
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        # Exception handling for API request failure
        print("Sorry, my speech service is down.")
        return ""
    except Exception as e:
        # General exception handling
        print(f"An error occurred in take_command: {e}")
        return ""

# Function to handle commands
def handle_command(command):
    if 'hello' in command or 'namaste' in command:
        response = 'Hi Rahul, how are you?'
    elif 'joke' in command:
        response = pyjokes.get_joke()
    elif 'play' in command:
        song = command.replace('play', '')
        response = 'Playing ' + song
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = current_time
    elif 'open' in command:
        command = command.replace('open', '')
        pyautogui.press('super')
        pyautogui.typewrite(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        response = 'opening ' + command
    elif 'close' in command:
        pyautogui.hotkey('alt', 'f4')
        response = 'Closing Sir!'
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        response = info
    elif 'remember that' in command:
        remember_message = command.replace('remember that', '').strip()
        new_message = RememberedMessage(message=remember_message)
        new_message.save()
        response = 'I will remember that ' + remember_message
    elif 'what do you remember' in command:
        messages = RememberedMessage.objects.all()
        if messages.exists():
            response = 'You told me to remember: ' + ' '.join([msg.message for msg in messages])
        else:
            response = 'I do not remember anything.'
    elif 'clear remember file' in command:
        RememberedMessage.objects.all().delete()
        response = 'All remembered messages have been deleted.'
    elif 'shutdown' in command:
        response = 'closing the pc in 3. 2. 1'
        os.system("shutdown /s /t 1")
    elif 'restart' in command:
        response = 'restarting the pc in 3. 2. 1'
        os.system("shutdown /r /t 1")
    elif "search" in command:
        usercm = command.replace("search", "")
        usercm = usercm.lower()
        webbrowser.open(f"{usercm}")
        response = 'this is what I found on the internet'
    elif "stop" in command or "start" in command:
        pyautogui.press('k')
        response = 'done'
    elif "full screen" in command:
        pyautogui.press('f')
        response = 'done'
    else:
        response = "I do not understand"

    talk(response)

# Function to continuously take commands
def continuous_listening():
    last_command = ""  # Variable to store the last processed command
    while True:
        command = take_command()  # Listen for a command
        if command and command != last_command:
            # Process the command only if it's different from the last command
            handle_command(command)
            last_command = command
        time.sleep(2)  # Adding a delay to avoid immediate re-processing

# Starting the continuous listening in a separate thread
threading.Thread(target=continuous_listening, daemon=True).start()

# Django views
def home(request):
    form = RememberMessageForm()
    if request.method == 'POST':
        form = RememberMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    messages = RememberedMessage.objects.all()
    return render(request, 'assistant/home.html', {'form': form, 'messages': messages})

def process_command(request):
    if request.method == 'POST':
        command = request.POST.get('command', '').lower()
        handle_command(command)
    return redirect('home')
