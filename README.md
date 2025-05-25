# NarraTone

**NarraTone** is a mood-based music companion for reading.

I enjoy listening to music while reading books, and I wanted an application that live-plays music based on what's happening in the story. Currently, NarraTone analyzes a single text snippet and plays matching music. I plan to integrate full EPUB support later on.

## Features

- Detects mood from a text passage (e.g., fear, joy, sadness)
- Plays a randomly chosen track from your local library based on detected mood
- Uses a DistilRoBERTa-based transformer model for emotion detection
- Uses Streamlit for a clean and simple interface

## Setup Instructions

### 1. Clone the repository

### 2. Set up a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

```bash
streamlit run app.py
```

## Music Folder Structure

Your music should go in this folder structure under `assets/music/`:

## What I'm Using

- **Emotion Detection Model**: `j-hartmann/emotion-english-distilroberta-base`
- **Frontend**: Streamlit
- **Audio Format**: MP3 files

## TODO

- Finish mapping all emotion tags to appropriate folders
- Get more copyright-free music tracks
- Add support for reading and parsing EPUBs
- Let users upload or assign their own tracks to emotion tags

## Notes

The emotion detection model is a transformer approach that analyzes text sentiment and emotional content. The app currently works with text snippets but the goal is full EPUB integration where music changes dynamically as you read through chapters.

Since I like quite moody classical music when I read, that's what I've used as my base collection. The customization feature will let people set their own music preferences for different emotional tags.
