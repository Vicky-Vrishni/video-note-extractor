import streamlit as st
from main import process_video
import os
st.title("📹 Video Note Extractor")
st.write("Upload a video or paste a YouTube link to get organized notes, timestamps, and action items.")

option = st.radio("Choose input type:", ["YouTube Link", "Upload Video File"])

video_input = None
is_url = True

if option == "YouTube Link":
    video_input = st.text_input("Paste YouTube URL here:")
    is_url = True
else:
    uploaded_file = st.file_uploader("Upload your video file", type=["mp4", "mov", "avi", "mkv"])
    if uploaded_file is not None:
        os.makedirs("uploads", exist_ok=True)
        video_input = os.path.join("uploads", uploaded_file.name)
        with open(video_input, "wb") as f:
            f.write(uploaded_file.getbuffer())
    is_url = False

if st.button("Generate Notes"):
    if video_input:
        with st.spinner("Processing video... This may take a few minutes."):
            try:
                notes = process_video(video_input, is_url=is_url)
                st.success("Notes generated successfully!")
                st.markdown("### 📝 Final Notes")
                st.write(notes)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please provide a YouTube link or upload a video file first.")

