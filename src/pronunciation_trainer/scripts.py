"""
This script is used to produce teacher audio files for the given examples using OpenAI's Text-to-Speech API.
The produced audio files are saved in the `audios/teacher` directory.
"""


from pathlib import Path

from openai import OpenAI

from pronunciation_trainer.config import openai_api_key
from pronunciation_trainer.loading import load_data
from pronunciation_trainer.rich_logging import log

data = load_data()

client = OpenAI(api_key=openai_api_key)


def produce_teacher_audio(audio_name, text):
    """
    Produce a teacher audio file for the given text using OpenAI's Text-to-Speech API.
    See: https://platform.openai.com/docs/guides/text-to-speech
    """

    speech_file_path = Path(f"audios/teacher/{audio_name}")
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="alloy",
        input=text,
    )

    response.stream_to_file(speech_file_path)
    log.info(
        f"Successfully produced teacher audio for {text=} at {speech_file_path.name=} 🎉"
    )


if __name__ == "__main__":
    # Produce teacher/ground-truth audio files for the given examples
    data = load_data()
    for datum in data:
        produce_teacher_audio(datum["learner_recording"], datum["text_to_record"])

    # Produce an additional example
    produce_teacher_audio("book.wav", "The book is on the table")
