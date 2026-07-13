# Music Chat Bot

A Flask-based chatbot that uses Google's Gemini API to answer music-related 
questions — artists, genres, theory, instruments, recommendations, and 
music history. Chat history is saved locally to a JSON file.

## Features
- Web interface for chatting (Flask + Jinja templates)
- Responses scoped to music topics via a system instruction
- Conversation history persisted to `chat_history.json`, with timestamps
- `/history` endpoint to retrieve past exchanges
- Error handling for failed API calls, both server-side and client-side

## Setup

1. Clone the repo and install dependencies:
   pip install flask google-generativeai python-dotenv

2. Get a free Gemini API key from https://aistudio.google.com/apikey

3. Create a `.env` file in the project root:
   GEMINI_API_KEY=your_key_here

4. Run the app:
   python app.py
   Visit http://localhost:5001

## Usage
- Ask anything music-related in the chat interface — genres, artists, 
  theory, instrument tips, recommendations
- Off-topic questions get redirected back to music by the bot
- All exchanges are saved to `chat_history.json` automatically
- GET `/history` returns the full conversation log as JSON

## Tech stack
- Backend: Flask
- AI: Google Gemini API (`gemini-2.5-flash`) with a music-scoped system instruction
- Storage: local JSON file
- Frontend: vanilla JS, DOM-based rendering (no raw HTML injection, avoids XSS)

## Notes
- API key is loaded from environment variables, never hardcoded
- `.env` and `chat_history.json` are excluded from version control
