from transformers import pipeline

emotion_detector = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def get_mood(text):
    result = emotion_detector(text)[0]  # Get list of scores
    best = max(result, key=lambda x: x["score"])
    return best["label"]