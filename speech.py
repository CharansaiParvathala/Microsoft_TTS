import edge_tts
from source import VOICES
import streamlit as st

OUTPUT_FILE_MP3 = "test.mp3"

async def save_speech(text: str, voice: str) -> None:
    if voice:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(OUTPUT_FILE_MP3)

def select_voice() -> str:
    language_choice = st.selectbox(
        'Select a Language:',
        ('choose your language', 'English', 'Spanish', 'French', 'German', 'Italian',
         'Portuguese', 'Dutch', 'Russian', 'Japanese', 'Chinese', 'Hindi', 'Arabic',
         'Turkish', 'Korean', 'Thai', 'Vietnamese', 'Bengali', 'Telugu', 'Tamil',
         'Malayalam', 'Swahili')
    )

    if language_choice != "choose your language":
        voices = [voice for voice in VOICES if voice.startswith(get_language_prefix(language_choice))]
        return select_voice_from_list(voices)

def get_language_prefix(language_choice: str) -> str:
    language_map = {
        "English": "en-", "Spanish": "es-", "French": "fr-", "German": "de-",
        "Italian": "it-", "Portuguese": "pt-", "Dutch": "nl-", "Russian": "ru-",
        "Japanese": "ja-", "Chinese": "zh-", "Hindi": "hi-", "Arabic": "ar-",
        "Turkish": "tr-", "Korean": "ko-", "Thai": "th-", "Vietnamese": "vi-",
        "Bengali": "bn-", "Telugu": "te-", "Tamil": "ta-", "Malayalam": "ml-",
        "Swahili": "sw-"
    }
    return language_map.get(language_choice, "")

def select_voice_from_list(voices: list) -> str:
    names = [voice.split('-')[-1].replace('Neural', '').strip() for voice in voices]
    choice = st.selectbox("Select a Voice:", names)
    if choice:
        return voices[names.index(choice)]
