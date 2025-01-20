import asyncio
import streamlit as st

from speech import save_speech, select_voice, OUTPUT_FILE_MP3
from pdf_read import read
from edge_tts.exceptions import *

def main():
    emp = st.empty()
    with st.sidebar:
        op = st.radio(
            "Choose One Mode",
            ("PDF to Speech", "Text to Speech")
        )

    pdf, text = None,''
    if op == 'PDF to Speech':
        pdf = st.file_uploader('Select your story file (PDF):', type='pdf')
        if pdf is not None:
            text = read(pdf)
            with st.expander('Edit Text'):
                text = st.text_area("Edit your Text:", value=text, height=300)
    elif op == 'Text to Speech':
        text = st.text_area("Enter your Text:", value=text, height=300)
        text += '\n\n***** End of the Page *****\n\n'

    if text != '':
        voice = select_voice()
        if voice != '' and voice != None:
            try:
                with st.expander("Audio Files:"):
                    with st.spinner("Prosseing Audio Files.."):
                        text = text.split('\n\n***** End of the Page *****\n\n')
                        for p in range(len(text) - 1):
                            c1,c2 = st.columns([5,1])
                            asyncio.run(save_speech(text[p], voice))
                            with open(OUTPUT_FILE_MP3, "rb") as file:
                                data = file.read()
                            c1.audio(OUTPUT_FILE_MP3,format='audio/mp3')
                            c2.download_button('Download',data=data, file_name=OUTPUT_FILE_MP3, mime="audio/mp3", key=str(p))
            except Exception as e:
                st.error(str(e))
if __name__ == "__main__":
    main()

