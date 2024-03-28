

from openai import OpenAI
from docx import Document
import streamlit as st

def transcribe_audio_with_whisper(audio_file_path):
  client = OpenAI(api_key="")
  audio_file= open("meeting.m4a", "rb")
  transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)


  return transcription.text


def summarize_text_with_gpt(text):
  client = OpenAI(api_key="")
    
    
  # Generate a summary of the transcribed text
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant that summarizes what is discussed in meetings. The following conversation is about SMTP Relay."},
    {"role": "user", "content": f"Please give a comprehensive summary of what was discussed in the following transcript of the following meeting. Make sure to organize using bullets and include any key action items: \n{text}"}])
  
    
  return response.choices[0].message.content.strip()

if __name__ == "__main__":
    
  st.title('Audio File Summarizer')
  audio_file_name = st.text_input('Enter the name of the audio file (including extension):')
  transcribed_text = transcribe_audio_with_whisper(audio_file_name)
  summary = summarize_text_with_gpt(transcribed_text)
  st.write(summary)
  doc = Document()
  doc.add_paragraph(summary)
  doc.save("Summary.docx")
  print("Transcribed Text:\n", transcribed_text)
  print("\nSummary:\n", summary)    
    

#%%





# %%
