from transformers import pipeline

class MoodDetector:
    def __init__(self):
        self.labels = ["base", "sad", "tense", "epic_battle"]
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def detect_mood(self, text):
        result = self.classifier(text, self.labels)
        top_mood = result['labels'][0]
        confidence = result['scores'][0]
        return top_mood, confidence