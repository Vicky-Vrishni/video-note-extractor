import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def generate_notes(transcript_text):
    prompt = f"""
You are an expert note-taker. Below is a transcript of a video/lecture.

Transcript:
{transcript_text}

Please provide:
1. Organized Notes (clear headings and bullet points summarizing key content)
2. Important Timestamps mentioned, if any context clues suggest key moments
3. Action Items / Tasks (any tasks, assignments, or things the listener should do)

Format your response with clear sections titled "Notes", "Important Points", and "Action Items".
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    sample_text = """
    I used to get a bullet but I don't know if you know that one.
    You know that one. You know how to shoot tea?
    """
    notes = generate_notes(sample_text)
    print(notes)