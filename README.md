# NarraTone

NarraTone detects the mood of a paragraph and plays music that matches it.

## What it does

- Uses a pre-trained AI model (facebook/bart-large-mnli) to classify paragraph mood
- Plays .mp3 files from a folder based on the detected mood
- Includes a simple GUI to paste text and listen

## Moods Supported

- sad
- happy
- scary
- fight
- neutral

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. (Linux only) Install tkinter separately if needed
