from extract_audio import download_audio, extract_audio_from_file
from transcribe import transcribe_audio
from generate_notes import generate_notes
def process_video(source, is_url=True):
    print("Step 1: Extracting audio...")
    if is_url:
        audio_path = download_audio(source)
    else:
        audio_path = extract_audio_from_file(source)
    print(f"Audio extracted: {audio_path}")

    print("Step 2: Transcribing audio...")
    result = transcribe_audio(audio_path)
    
    transcript_with_timestamps = ""
    for segment in result.segments:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        transcript_with_timestamps += f"[{start:.1f}s - {end:.1f}s] {text}\n"
        
    print("Transcription complete.")

    print("Step 3: Generating notes...")
    notes = generate_notes(transcript_with_timestamps)
    print("Notes generated.")

    return notes
if __name__ == "__main__":
    video_path = r"E:\20250114_155913.mp4"
    final_notes = process_video(video_path, is_url=False)
    
    print("\n========== FINAL NOTES ==========\n")
    print(final_notes)
    