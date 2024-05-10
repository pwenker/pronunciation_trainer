"""
This module contains the code to create a language model chain using the OpenAI API.
"""


from pathlib import Path

import gradio as gr
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from pronunciation_trainer.config import openai_api_key

prompt = ChatPromptTemplate.from_template(Path("prompt.md").read_text())
output_parser = StrOutputParser()


def create_llm(openai_api_key=openai_api_key):
    if openai_api_key in [None, ""]:
        raise gr.Error(
            "No API key provided! You can find your API key at https://platform.openai.com/account/api-keys."
        )
    llm = ChatOpenAI(model="gpt-4-turbo", openai_api_key=openai_api_key)
    return llm


def create_llm_chain(prompt=prompt, output_parser=output_parser, openai_api_key=openai_api_key):
    if openai_api_key in [None, ""]:
        raise gr.Error(
            """No API key provided! You can find your API key at https://platform.openai.com/account/api-keys."""
        )
    llm = ChatOpenAI(model="gpt-4-turbo", openai_api_key=openai_api_key)
    llm_chain = prompt | llm | output_parser
    return llm_chain
