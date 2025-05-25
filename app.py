import os
import streamlit as st
from mood import get_mood
from music import get_music_tag, get_random_track

st.set_page_config(page_title="NarraTone", layout="centered")
st.title("🎵 NarraTone Mood-Based Music for Reading")

text_input = st.text_area("Enter a scene from your book:", height=200)

if st.button("Detect Mood & Play Music") and text_input.strip():
    mood = get_mood(text_input)
    st.markdown(f"**Detected Mood:** `{mood}`")

    folder = get_music_tag(mood)
    track_path = get_random_track(folder, base_path="assets/music")

    if track_path and os.path.exists(track_path):
        with open(track_path, 'rb') as f:
            audio_bytes = f.read()

        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
        st.success(f"Now playing: `{os.path.basename(track_path)}` from `{folder}/`")
    else:
        st.error("No music file found for this mood. Check the folder or add some `.mp3` files.")
