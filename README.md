# Voice Operated Assistant (VOA)

Welcome to the Voice Operated Assistant (VOA) project! This Python-based application is designed to revolutionize human-computer interaction by leveraging advanced speech recognition and natural language processing (NLP) technologies. 

VOA is your intelligent virtual assistant, capable of understanding voice commands, performing automated tasks, and providing personalized assistance seamlessly.

---

## Key Features

- **Natural Language Processing**: Understands and processes user commands in natural language.
- **Speech Recognition**: Converts speech to text for enhanced interaction.
- **Task Automation**: Executes commands like playing music, fetching information, opening applications, and more.
- **Personalization**: Learns user preferences over time.
- **Continuous Learning**: Adapts and improves with regular use.

---

## Functionality

### Core Features

1. **Greeting the User**: Greets based on the time of day.
2. **Command Recognition**: Accepts and processes voice commands.
3. **Task Execution**: Performs tasks such as:
   - Playing music on YouTube
   - Fetching jokes
   - Providing the current time and date
   - Searching Wikipedia
   - Automating GUI tasks
   - Opening applications or websites
4. **Custom Memory**: Remembers specific user-provided information during the session.
5. **System Controls**: Can shut down, restart, or log off the computer via voice commands.
6. **Error Handling**: Gracefully handles errors and unexpected inputs.

---

## Libraries Used

- **[pyttsx3](https://pypi.org/project/pyttsx3/)**: Text-to-speech conversion.
- **[speech_recognition](https://pypi.org/project/SpeechRecognition/)**: Speech-to-text processing.
- **[datetime](https://docs.python.org/3/library/datetime.html)**: Handling dates and times.
- **[pyjokes](https://pypi.org/project/pyjokes/)**: Fetching random jokes.
- **[pywhatkit](https://pypi.org/project/pywhatkit/)**: Web-based task automation (e.g., YouTube commands).
- **[pyautogui](https://pypi.org/project/PyAutoGUI/)**: GUI automation for mouse and keyboard operations.
- **[wikipedia](https://pypi.org/project/wikipedia-api/)**: Fetching information from Wikipedia.
- **[os](https://docs.python.org/3/library/os.html)**: Interfacing with the operating system.
- **[webbrowser](https://docs.python.org/3/library/webbrowser.html)**: Opening web browsers.

---

## Project Structure

```
DjangoVOA/
│
├── env/  				   # Virtual environment
├── VoiceAssistantProject/     	   # Main project folder
│   ├── assistant/             	   # App folder
│   │   ├── __pycache__/       	   # Compiled Python files
│   │   ├── migrations/        	   # Database migrations
│   │   ├── templates/         	   # HTML templates
│   │   │   ├── assistant/     	   # Templates for the assistant app
│   │   │   │   ├── home.html
│   │   │   ├── static/        	   # Static assets
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── VoiceAssistantProject/ 	   # Project configuration
│   │   ├── __pycache__/       
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3             	   # SQLite database
│   ├── manage.py              	   # Django management script
├── remember.txt               	   # Notes or persistent memory file
```

---

## Usage Instructions

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd DjangoVOA
   ```
2. Set up the virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Django server:
   ```bash
   python manage.py runserver
   ```
5. Access the application:
   Open `http://127.0.0.1:8000` in your web browser.

---

## Demo

For a visual demonstration of the project, check out our [YouTube Demo](https://www.youtube.com/watch?v=Mc1FstS_U74&t=35s).

---

## Conclusion

Voice Operated Assistant (VOA) is designed to simplify daily tasks through intuitive voice interactions. Its scalable and extensible design ensures seamless integration of future enhancements and new features. Start using VOA today for an efficient, hands-free experience!

---

## License

This project is licensed under the MIT License.

---

## Contributors

- **Rahul Prasad** (Project Lead)
- Team Members: *[Add names here]*

Feel free to contribute and improve VOA by submitting pull requests or reporting issues!
