## FastAPI & Whisper Audio Transcription and AI Answering

This repository contains a FastAPI application for transcribing audio files and generating AI-powered answers based on the transcribed text. The application utilizes the OpenAI API for generating answers.

### Features

- Transcribe uploaded audio files to text.
- Utilize OpenAI API for generating AI answers based on the transcribed text.
- Cross-Origin Resource Sharing (CORS) middleware for allowing requests from any origin.

### Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Install the required Python libraries:

   ```bash
   pip install fastapi uvicorn openai whisper
   ```

3. Set up your OpenAI API key. You can obtain your API key from the [OpenAI website](https://openai.com).

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

### Usage

1. Upload an audio file using the provided HTML interface.
2. Provide your OpenAI API key for generating AI answers.
3. The audio file will be transcribed, and the transcribed text will be used as input for generating AI answers.
4. View the generated answers in the API response.

### Repository Structure

- `main.py`: FastAPI application code for audio transcription and AI answering.
- `index.html`: HTML template for the homepage.
- `README.md`: Documentation providing setup instructions and usage guidelines.

### Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): Web framework for building APIs with Python.
- [Uvicorn](https://www.uvicorn.org/): ASGI server for running FastAPI applications.
- [OpenAI](https://openai.com): AI models and API for generating natural language responses.
- [Whisper](https://pypi.org/project/whisper/): Library for transcribing audio files.

### Acknowledgments

- This project relies on FastAPI and OpenAI for building the audio transcription and AI answering functionality.
- The Whisper library is used for transcribing audio files.

Feel free to explore, modify, and extend this project according to your requirements. If you have any questions or suggestions, please feel free to reach out!
