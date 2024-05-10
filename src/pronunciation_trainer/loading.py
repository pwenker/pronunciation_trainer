"""
This module is responsible for loading data from the provided JSON file.
It also provides functions to load simple and advanced examples for the grapheme-based 
and phoneme-based pronunciation trainer, respectively.
"""
import json


def load_data(filepath: str = "learner_input.json") -> dict:
    with open(filepath, "r") as file:
        data = json.load(file)
    return data


def load_simple_examples():
    simple_examples = [
        [
            ex["text_to_record"],
            ex["sr_transcript_of_learner_recording"],
        ]
        for ex in load_data()
    ]
    return simple_examples


def load_advanced_examples():
    advanced_examples = [
        [
            "Lithuanian",
            "English",
            f'audios/learner/{ex["learner_recording"]}',
            f'audios/teacher/{ex["learner_recording"]}',
        ]
        for ex in load_data()
    ]
    advanced_examples.append(
        [
            "German",
            "English",
            f"audios/learner/book.aac",
            f"audios/teacher/book.wav",
        ]
    )
    return advanced_examples
