# 📹 Video Note Extractor

An AI-powered video note-taking tool that converts lectures, tutorials, and other video content into **organized notes, important points, timestamps, and action items**.

The application supports both **YouTube URLs** and **local video uploads** through a simple Streamlit interface.

---

## 🚀 Features

* 🎥 **YouTube Video Support** — Paste a YouTube video URL and process it.
* 📁 **Local Video Upload** — Upload videos in MP4, MOV, AVI, or MKV format.
* 🔊 **Automatic Audio Extraction** — Extracts audio from the provided video.
* 🎙️ **AI Transcription** — Converts speech into text using Groq's Whisper Large V3 model.
* ⏱️ **Timestamped Transcription** — Keeps track of the start and end time of each transcript segment.
* 📝 **AI-Generated Notes** — Converts the transcript into structured notes.
* 💡 **Important Points** — Extracts the key concepts from the video.
* ✅ **Action Items** — Identifies tasks, assignments, or things that need to be done.
* 🖥️ **Simple Streamlit UI** — Easy-to-use web interface for processing videos.

---

## 🧠 How It Works

The application follows a simple AI-powered processing pipeline:

```text
              ┌───────────────────┐
              │   Video Input     │
              │                   │
              │ YouTube URL /     │
              │ Local Video File  │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │  Audio Extraction │
              │                   │
              │ yt-dlp / FFmpeg   │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │    Transcription  │
              │                   │
              │ Whisper Large V3  │
              │    via Groq       │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Transcript +      │
              │    Timestamps     │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │  Note Generation  │
              │                   │
              │ Llama 3.1 8B      │
              │    via Groq       │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │   Final Notes     │
              │                   │
              │ • Notes           │
              │ • Important Points│
              │ • Action Items    │
              └───────────────────┘
```

---

## 🛠️ Tech Stack

| Technology               | Purpose                         |
| ------------------------ | ------------------------------- |
| **Python**               | Core application logic          |
| **Streamlit**            | Web interface                   |
| **yt-dlp**               | YouTube video/audio downloading |
| **FFmpeg**               | Audio extraction and conversion |
| **Groq API**             | AI inference                    |
| **Whisper Large V3**     | Speech-to-text transcription    |
| **Llama 3.1 8B Instant** | AI-powered note generation      |
| **python-dotenv**        | Environment variable management |

---

## 📂 Project Structure

```text
video-note-extractor/
│
├── app.py                 # Streamlit user interface
├── main.py                # Main video-processing pipeline
├── extract_audio.py       # Audio extraction/download logic
├── transcribe.py          # Speech-to-text transcription
├── generate_notes.py      # AI-based note generation
│
├── requirements.txt       # Python dependencies
├── packages.txt           # System packages
├── cookies.txt            # YouTube authentication cookies
├── .gitignore
│
└── .devcontainer/         # Development container configuration
```

---

## 🔄 Processing Pipeline

### 1. Input Video

The application accepts either:

* A YouTube URL
* A locally uploaded video file

The Streamlit interface provides both options.

### 2. Audio Extraction

For YouTube videos, `yt-dlp` downloads the best available audio and converts it into WAV format.

For uploaded video files, FFmpeg extracts the audio and converts it to a format suitable for transcription.

### 3. Speech-to-Text

The extracted audio is sent to the **Whisper Large V3** model through the Groq API.

The transcription uses a verbose JSON response so that timestamp information can also be retrieved.

Example:

```text
[10.2s - 15.7s] Machine learning is a subset of artificial intelligence...
[15.7s - 22.4s] It allows systems to learn from data...
```

### 4. AI Note Generation

The timestamped transcript is passed to **Llama 3.1 8B Instant** through the Groq API.

The model is instructed to generate:

* Organized Notes
* Important Points
* Action Items

The final result is displayed directly in the Streamlit application.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Vicky-Vrishni/video-note-extractor.git
```

Move into the project directory:

```bash
cd video-note-extractor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

FFmpeg is required for extracting audio from video files.

Make sure FFmpeg is installed and available in your system PATH.

You can verify the installation with:

```bash
ffmpeg -version
```

---

## 🔑 Environment Variables

The project uses the Groq API for both transcription and AI note generation.

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can obtain a Groq API key from the Groq developer platform.

> ⚠️ Never commit your actual API key to GitHub.

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

After starting the application, open the URL provided by Streamlit in your browser.

---

## 🖥️ Usage

### Option 1 — YouTube Video

1. Select **YouTube Link**.
2. Paste the YouTube URL.
3. Click **Generate Notes**.
4. Wait for the video to be processed.
5. View the generated notes.

### Option 2 — Local Video

1. Select **Upload Video File**.
2. Upload an MP4, MOV, AVI, or MKV file.
3. Click **Generate Notes**.
4. Wait for processing to complete.
5. View the generated notes.

---

## 📄 Example Output

The generated result is structured into sections such as:

```text
Notes
-----

• Introduction to Machine Learning
• Supervised and Unsupervised Learning
• Training data and testing data
• Model evaluation


Important Points
----------------

• Machine learning learns patterns from data.
• Training and testing datasets serve different purposes.
• Model performance should be evaluated on unseen data.


Action Items
------------

• Review supervised learning algorithms.
• Practice with a sample dataset.
• Implement a basic classification model.
```

---

## ⚠️ YouTube Limitations

YouTube videos may sometimes fail to download because of restrictions, authentication requirements, or limitations imposed on cloud/server environments.

If a YouTube URL cannot be processed, the application recommends uploading the video file directly instead.

For YouTube downloads, the project also uses a `cookies.txt` file when configured.

---

## 🔐 Security Notes

* Keep your `GROQ_API_KEY` private.
* Do not upload API keys to GitHub.
* Avoid committing sensitive YouTube cookies.
* Add sensitive files to `.gitignore` when appropriate.

---

## 🎯 Use Cases

This project can be useful for:

* 🎓 Students taking online lectures
* 💻 Programming tutorials
* 📚 Educational videos
* 🧑‍💼 Meetings and presentations
* 📝 Quick revision material
* 🎥 Long-form educational content
* 📖 Self-learning and research

---

## 🚧 Future Improvements

Potential improvements include:

* [ ] Download generated notes as PDF
* [ ] Export notes as Markdown
* [ ] Generate short summaries
* [ ] Add chapter-wise video segmentation
* [ ] Add searchable transcripts
* [ ] Generate quiz questions from videos
* [ ] Generate flashcards automatically
* [ ] Support multiple languages
* [ ] Add a chat interface for asking questions about the video
* [ ] Improve YouTube authentication and download reliability
* [ ] Deploy the application with a production-ready backend

---

## 🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

```bash
git checkout -b feature/your-feature
```

Make your changes, commit them, and open a pull request.

---

## 📜 License

This project is open-source and available under the terms of the license included in this repository.

---


# Sample Video Notes

## Video Summary

This video explains the fundamentals of machine learning and how models learn patterns from data.

## Key Points

* Machine learning enables systems to learn from data.
* Supervised learning uses labeled datasets.
* Unsupervised learning identifies hidden patterns.
* Model evaluation helps measure performance.

## Action Items

* Review the difference between supervised and unsupervised learning.
* Practice training a simple machine learning model.
* Explore model evaluation metrics.

## Important Concepts

* Machine Learning
* Training Dataset
* Model Evaluation
* Predictive Modeling


## 👨‍💻 Author

**Vicky Vrishni**

GitHub:
https://github.com/Vicky-Vrishni

Project Repository:
https://github.com/Vicky-Vrishni/video-note-extractor

