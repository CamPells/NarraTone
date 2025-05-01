import tkinter as tk
from tkinter import scrolledtext
from mood import MoodDetector
from music import MusicPlayer

def start_gui():
    detector = MoodDetector()
    player = MusicPlayer()

    def on_submit():
        paragraph = input_box.get("1.0", tk.END).strip()
        if not paragraph:
            return

        mood, confidence = detector.detect_mood(paragraph)
        mood_label.config(text=f"Mood: {mood} ({confidence:.2f})")

        if confidence >= 0.4:
            player.play_music(mood)

    root = tk.Tk()
    root.title("NarraTone")
    root.geometry("600x400")

    input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
    input_box.pack(padx=10, pady=10)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=5)

    mood_label = tk.Label(root, text="Mood: ", font=("Arial", 12))
    mood_label.pack(pady=5)

    root.mainloop()
