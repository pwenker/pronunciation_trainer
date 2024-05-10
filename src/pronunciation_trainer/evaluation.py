"""
This module provides functions for evaluating speaking attempts.

It includes:
- A basic evaluation function that compares two phrases (grapheme-based) and provides feedback based on their similarity ratio.
- An advanced evaluation function that uses a language learning model (LLM) to provide feedback based on phoneme transcriptions.

The basic evaluation function includes:
- A normalization function that converts input texts to lower case and strips whitespace.
- A function that calculates the similarity ratio between two phrases.
- A function that generates a diff between two phrases.
- A function that generates feedback based on the similarity ratio.

The advanced evaluation function includes:
- A function that invokes an LLM chain to provide phoneme-based feedback
"""


from difflib import Differ, SequenceMatcher
from typing import Optional, Tuple

from pronunciation_trainer.llm import create_llm_chain


def normalize_texts(actual: str, expected: str) -> list[str]:
    """Normalize two input texts by converting them to lower case and stripping whitespace.

    Note: This normalization function is very simple and only here to demonstrate the general necessity of normalization
    """

    return [text.lower().strip() for text in [actual, expected]]


def compare_phrases(expected: str, actual: str) -> float:
    """Calculate the similarity ratio between two phrases."""
    return SequenceMatcher(None, expected, actual).ratio()


def diff_phrases(expected: str, actual: str) -> list[Tuple[str, Optional[str]]]:
    """Generate a diff between two phrases."""
    differ = Differ()
    return [
        (token[2:], None if token[0] == " " else token[0])
        for token in differ.compare(expected, actual)
    ]


def generate_feedback(similarity_ratio: float) -> str:
    """Generate feedback based on the similarity ratio."""
    if similarity_ratio > 0.9:
        return "Excellent!"
    elif similarity_ratio > 0.7:
        return "Good job!"
    elif similarity_ratio > 0.5:
        return "Not bad, but there's room for improvement."
    else:
        return "Please try again, focus on pronunciation and clarity."


def basic_evaluation(
    expected: str, actual: str, autojunk: bool = True
) -> Tuple[float, str, list[Tuple[str, Optional[str]]]]:
    """Evaluate speaking attempts by comparing expected and actual phrases."""
    expected, actual = normalize_texts(expected, actual)
    similarity_ratio = compare_phrases(expected, actual)
    diff = diff_phrases(expected, actual)
    feedback = generate_feedback(similarity_ratio)
    return similarity_ratio, feedback, diff


def advanced_evaluation(
    learner_l1,
    learner_l2,
    learner_phoneme_transcription,
    teacher_phoneme_transcription,
) -> str:
    """Provide LLM-based feedback"""
    return create_llm_chain().invoke(
        {
            "learner_l1": learner_l1,
            "learner_l2": learner_l2,
            "learner_phoneme_transcription": learner_phoneme_transcription,
            "teacher_phoneme_transcription": teacher_phoneme_transcription,
        }
    )
