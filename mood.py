from transformers import pipeline

class MoodDetector:
    def __init__(self):
        self.labels = ["sad", "happy", "scary", "tense", "fight", "neutral"]
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def detect_mood(self, text):
        result = self.classifier(text, self.labels)
        label = result['labels'][0]
        if label == "scary":
            label = "tense"
        return label, result['scores'][0]