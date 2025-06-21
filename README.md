## README.md

# Voice Assistant (alex.py)

A simple Python voice assistant that listens to your commands, speaks responses, and can perform basic tasks like telling the time, opening websites, and playing music.

---

## Description

This project is a beginner-friendly voice assistant built with Python. It uses speech recognition and text-to-speech to interact with users and can perform simple tasks such as telling the time, announcing the date, opening popular websites (Google, YouTube, Spotify), and playing music from a local folder.

---

## Features

- Listens to your voice commands
- Speaks responses using text-to-speech
- Tells the current time and date
- Opens Google, YouTube, or Spotify in your web browser
- Plays music from your local music folder
- Friendly greetings based on the time of day
- Simple error handling for unrecognized commands

---

## Requirements

- Python 3.x
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)

You can install the required packages using pip:

```bash
pip install SpeechRecognition pyttsx3
```

You may also need to install PyAudio for microphone support:

```bash
pip install pyaudio
```
If you have issues installing PyAudio, refer to its documentation for platform-specific instructions.

---

## Usage

1. Clone or download this repository.
2. Open `alex.py` in your preferred Python environment.
3. Edit the `music_folder` path in the `play music` section to match your local music directory.
4. Run the script:

```bash
python alex.py
```

5. Speak commands such as:
   - "What time is it?"
   - "What's the date?"
   - "Open Google"
   - "Open YouTube"
   - "Play music"
   - "Exit" or "Stop" to quit

---

## Simple Description

A beginner-friendly Python voice assistant that listens to your voice, speaks responses, and helps you with basic tasks like telling the time, opening websites, and playing music.

---

## Notes

- Make sure your microphone is connected and working.
- The assistant uses Google’s speech recognition API, so an internet connection is required for voice input.
- For music playback, update the `music_folder` path to point to your own music files.

---

## License

This project is open-source and free to use.

---

Feel free to customize the assistant or add more commands as you learn!

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/56396120/88fe0705-74c5-4324-b0cc-964862245773/alex.py
