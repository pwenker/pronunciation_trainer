"""
This module contains the transcribe function, which uses the Hugging Face pipeline to transcribe audio to text.

The transcribe function takes a single parameter, audio, which is a numpy array of the audio the user recorded.

There are two transcriber choices available: grapheme and phoneme. The grapheme transcriber uses the openai/whisper-base.en model, while the phoneme transcriber uses the facebook/wav2vec2-lv-60-espeak-cv-ft model.
"""
from enum import StrEnum
from functools import partial

import numpy as np
from transformers import pipeline


class TranscriberChoice(StrEnum):
    grapheme = "openai/whisper-base.en"
    phoneme = "facebook/wav2vec2-lv-60-espeak-cv-ft"


def transcribe(
    audio, transcriber_choice: TranscriberChoice = TranscriberChoice.grapheme
):
    """
    The transcribe function takes a single parameter, audio, which is a numpy array of the audio the user recorded.
    The pipeline object expects this in float32 format,so we convert it first to float32, and then extract the transcribed text.
    """
    transcriber = pipeline("automatic-speech-recognition", model=transcriber_choice)
    try:
        sr, y = audio
        print(f"Sampling rate is {sr}")
    except TypeError:
        return None
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))
    transcription = transcriber({"sampling_rate": sr, "raw": y})["text"]
    return transcription


transcribe_to_phonemes = partial(
    transcribe, transcriber_choice=TranscriberChoice.phoneme
)
transcribe_to_graphemes = partial(
    transcribe, transcriber_choice=TranscriberChoice.grapheme
)
