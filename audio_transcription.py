import os
from huggingface_hub import login
from pyannote.audio import Pipeline
from pyannote.core import Segment
from pyannote.audio import Audio
import whisper

def transcribe_audio(file_path: str) -> str:
    ACCESS_TOKEN = "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"

    # Check if audio file exists
    if not os.path.exists(file_path):
        return f"Audio file not found: {file_path}"

    # Authenticate with Huggingface Hub
    try:
        login(token=ACCESS_TOKEN, add_to_git_credential=True)
        print("Hugging Face authentication successful.")
    except Exception as e:
        return f"Error during Hugging Face authentication: {str(e)}"

    # Load speaker diarization model
    try:
        speaker_diarization = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1", use_auth_token=ACCESS_TOKEN)
        if speaker_diarization is None:
            return "Error: Speaker diarization model is None."
        print("Speaker diarization model loaded successfully.")
    except Exception as e:
        return f"Error loading speaker diarization model: {str(e)}"

    # Apply speaker diarization
    try:
        who_speaks_when = speaker_diarization(file_path, num_speakers=None, min_speakers=None, max_speakers=None)
    except Exception as e:
        return f"Error during speaker diarization: {str(e)}"

    # Load OpenAI Whisper model
    try:
        model = whisper.load_model("tiny.en")
        print("OpenAI Whisper model loaded successfully.")
    except Exception as e:
        return f"Error loading OpenAI Whisper model: {str(e)}"

    # Transcribe using speaker segmentation
    first_minute = Segment(0, 120)
    audio = Audio(sample_rate=16000, mono=True)
    transcript = ""

    for segment, _, speaker in who_speaks_when.crop(first_minute).itertracks(yield_label=True):
        try:
            waveform, sample_rate = audio.crop(file_path, segment)
            text = model.transcribe(waveform.squeeze().numpy())["text"]
            transcript += f"{segment.start:06.1f}s {segment.end:06.1f}s {speaker}: {text}\n"
        except Exception as e:
            return f"Error during transcription for segment {segment}: {str(e)}"

    return transcript
