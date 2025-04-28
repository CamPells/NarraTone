from mood import MoodDetector

def main():
    detector = MoodDetector()

    print("Welcome to NarraTone Mood Detector!")
    print("Paste a paragraph to analyze the mood, or type 'exit' to quit.")

    while True:
        paragraph = input("\nEnter paragraph: ")

        if paragraph.lower() == 'exit':
            print("Goodbye!")
            break

        mood, confidence = detector.detect_mood(paragraph)
        print(f"Detected mood: {mood} (Confidence: {confidence:.2f})")

if __name__ == "__main__":
    main()