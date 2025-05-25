import os
import random

def get_music_tag(mood):
    mapping = {
        "joy": "base",
        "sadness": "sad",
        "anger": "epic_battle",
        "fear": "tense_horror",
        "love": "base",
        "neutral": "base"
    }
    return mapping.get(mood.lower(), "base")

def get_random_track(folder, base_path="assets/music"):
    if not folder:
        print("No folder passed in.")
        return None

    folder_path = os.path.join(base_path, folder)
    print(f"Looking in: {folder_path}")

    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return None

    tracks = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    print(f"Found tracks: {tracks}")

    if not tracks:
        print(f"No MP3 files in: {folder_path}")
        return None

    return os.path.join(folder_path, random.choice(tracks))
