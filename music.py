import os
import random
import pygame

class MusicPlayer:
    def __init__(self, music_folder="assets/music"):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.current_mood = None

    def play_music(self, mood):
        path = os.path.join(self.music_folder, mood)
        if not os.path.isdir(path):
            return

        tracks = [f for f in os.listdir(path) if f.endswith(".mp3")]
        if not tracks:
            return

        if mood == self.current_mood:
            return

        pygame.mixer.music.stop()
        pygame.mixer.music.load(os.path.join(path, random.choice(tracks)))
        pygame.mixer.music.play(-1)
        self.current_mood = mood
