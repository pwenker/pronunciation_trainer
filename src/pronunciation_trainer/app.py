"""
This script provides a simple web interface for the pronunciation trainer using the gradio library
"""


from pathlib import Path

import os
import gradio as gr
from phonemizer import phonemize

from pronunciation_trainer.evaluation import (advanced_evaluation,
                                              basic_evaluation,
                                              normalize_texts)
from pronunciation_trainer.loading import (load_advanced_examples,
                                           load_simple_examples)
from pronunciation_trainer.transcription import (transcribe_to_graphemes,
                                                 transcribe_to_phonemes)

with gr.Blocks() as demo:
    with gr.Tab("Welcome"):
        readme = Path("README.md").read_text()
        gr.Markdown(readme)

    with gr.Tab("Grapheme-Based Speech Evaluation"):
        with gr.Row():
            learner_transcription = gr.Textbox(
                label="Learner Transcription",
                placeholder="It is nice to wreck a nice beach",
            )
            teacher_transcription = gr.Textbox(
                label="Teacher Transcription",
                placeholder="It is nice to recognize speech",
            )
        basic_evaluate_btn = gr.Button("Evaluate", variant="primary")
        gr.Markdown("## Evaluation")
        gr.Markdown("### Basic Evaluation")
        grapheme_evaluation = gr.Markdown()
        with gr.Row():
            basic_similarity_score = gr.Label(label="Similarity Score of Transcripts")
            basic_diff_box = gr.HighlightedText(
                label="Difference between Learner and Teacher transcripts",
                combine_adjacent=True,
                show_legend=True,
                color_map={"+": "red", "-": "green"},
            )
        basic_evaluate_btn.click(
            fn=normalize_texts,
            inputs=[learner_transcription, teacher_transcription],
            outputs=[learner_transcription, teacher_transcription],
        ).success(
            fn=basic_evaluation,
            inputs=[learner_transcription, teacher_transcription],
            outputs=[basic_similarity_score, grapheme_evaluation, basic_diff_box],
        )
        with gr.Accordion("Learner Examples"):
            gr.Markdown("### Examples for grapheme-based evaluation")
            simple_examples = gr.Examples(
                examples=load_simple_examples(),
                inputs=[
                    teacher_transcription,
                    learner_transcription,
                ],
            )
    with gr.Tab("Phoneme-Based Speech Evaluation"):
        with gr.Row():
            learner_recording = gr.Audio(
                label="Learner Recording",
                sources=["microphone", "upload"],
            )
            teacher_recording = gr.Audio(
                label="Teacher Recording",
                sources=["microphone", "upload"],
            )
        with gr.Row():
            learner_phoneme_transcription = gr.Textbox(
                label="Learner Phoneme Transcription",
                placeholder=phonemize(learner_transcription.placeholder),
                interactive=True,
            )
            teacher_phoneme_transcription = gr.Textbox(
                label="Teacher Phoneme Transcription",
                placeholder=phonemize(teacher_transcription.placeholder),
                interactive=True,
            )
        learner_l1 = gr.Textbox(
            label="Native language of  Learner (L1)", placeholder="German"
        )
        learner_l2 = gr.Textbox(
            label="Language the learner aims to acquire (L2)", placeholder="English"
        )
        openai_api_key = gr.Textbox(
                placeholder="Paste your OpenAI API key (sk-...)",
                show_label=False,
                value=os.getenv("OPENAI_API_KEY"),
                label="openai_api_key",
                lines=1,
                type="password",
            )
        
        advanced_evaluate_btn = gr.Button("Evaluate", variant="primary")
        gr.Markdown("## Advanced Evaluation")

        with gr.Row():
            similarity_score = gr.Label(
                label="Similarity Score of of Phoneme Transcripts"
            )
            diff_box = gr.HighlightedText(
                label="Difference between Learner and Teacher Phoneme transcripts",
                combine_adjacent=True,
                show_legend=True,
                color_map={"+": "red", "-": "green"},
            )
        llm_evaluation = gr.Markdown()

        learner_recording.change(
            fn=transcribe_to_phonemes,
            inputs=learner_recording,
            outputs=learner_phoneme_transcription,
        )
        teacher_recording.change(
            fn=transcribe_to_phonemes,
            inputs=teacher_recording,
            outputs=teacher_phoneme_transcription,
        )

        advanced_evaluate_btn.click(
            fn=basic_evaluation,
            inputs=[learner_phoneme_transcription, teacher_phoneme_transcription],
            outputs=[similarity_score, llm_evaluation, diff_box],
        ).success(
            advanced_evaluation,
            inputs=[
                learner_l1,
                learner_l2,
                learner_phoneme_transcription,
                teacher_phoneme_transcription,
                openai_api_key,
            ],
            outputs=llm_evaluation,
        )
        with gr.Accordion("Learner Examples"):
            gr.Markdown("### Examples for advanced evaluation")
            advanced_examples = gr.Examples(
                examples=load_advanced_examples(),
                inputs=[
                    learner_l1,
                    learner_l2,
                    learner_recording,
                    teacher_recording,
                ],
            )

if __name__ == "__main__":
    demo.launch()
