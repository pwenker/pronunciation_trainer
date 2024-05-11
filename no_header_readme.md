# Pronunciation Trainer 🗣️

This repository/app showcases how a [phoneme-based pronunciation trainer](https://github.com/pwenker/pronunciation_trainer/blob/main/docs/phoneme_based_solution.md)
(including personalized LLM-based feedback) overcomes the limitations of a [grapheme-based approach](https://github.com/pwenker/pronunciation_trainer/blob/main/docs/grapheme_based_solution.md)

For convenience, you find a feature comparison overview of the two solutions below:

| Feature                           | Grapheme-Based Solution                                  | Phoneme-Based Solution                                  |
|-----------------------------------|----------------------------------------------------------|---------------------------------------------------------|
| **Input Type**                    | Text transcriptions of speech                            | Audio files and phoneme transcriptions                  |
| **Feedback Mechanism**            | Comparison of grapheme sequences                         | Comparison of phoneme sequences and advanced LLM-based feedback |
| **Technological Approach**        | Simple text comparison using `SequenceMatcher`           | Advanced ASR models like Wav2Vec2 for phoneme recognition |
| **Feedback Detail**               | Basic similarity score and diff                          | Detailed phoneme comparison, LLM-based feedback including motivational and corrective elements |
| **Error Sensitivity**             | Sensitive to homophones and transcription errors         | More accurate in capturing pronunciation nuances        |
| **Suprasegmental Features**       | Does not capture (stress, intonation)                    | Potentially captures through phoneme dynamics and advanced evaluation |
| **Personalization**               | Limited to error feedback based on text similarity       | Advanced personalization considering learner's native language and target language proficiency |
| **Scalability**                   | Easy to scale with basic text processing tools           | Requires more computational resources for ASR and LLM processing |
| **Cost**                          | Lower, primarily involves basic computational resources   | Higher, due to usage of advanced APIs and model processing |
| **Accuracy**                      | Lower, prone to misinterpretations of homophones         | Higher, better at handling diverse pronunciation patterns (but LLM hallucinations) |
| **Feedback Quality**              | Basic, often not linguistically rich                     | Rich, detailed, personalized, and linguistically informed              |
| **Potential for Learning**        | Limited to recognizing text differences                   | High, includes phonetic and prosodic feedback, as well as resource and practice recommendations           |

## Quickstart 🚀

### 👉 Click here to try out the app directly:
[**Pronunciation Trainer App**](https://pwenker-pronunciation-trainer.hf.space/)

### 🔍 Inspect the code at:
- **GitHub:** [pwenker/pronunciation_trainer](https://github.com/pwenker/pronunciation_trainer)
- **Hugging Face Spaces:** [pwenker/pronunciation_trainer](https://huggingface.co/spaces/pwenker/pronunciation_trainer)

### 📚 Read about the pronunciation trainer:

1. [Grapheme-based Approach](https://github.com/pwenker/pronunciation_trainer/blob/main/docs/grapheme_based_solution.md)
2. [Phoneme-based Approach](https://github.com/pwenker/pronunciation_trainer/blob/main/docs/phoneme_based_solution.md)


## Local Deployment 🏠

### Prerequisites 📋

#### Rye 🌾
[Install `Rye`](https://rye-up.com/guide/installation/#installing-rye)
> Rye is a comprehensive tool designed for Python developers. It simplifies your workflow by managing Python installations and dependencies. Simply install Rye, and it takes care of the rest.

- Create a `.env` file in the `pronunciation_trainer` folder and add the following variable:

#### OPENAI API Token 🔑
```
OPENAI_TOKEN=... # Token for the OpenAI API
```

### Set-Up 🛠️

Clone the repository:
```
git clone [repository-url] # Replace [repository-url] with the actual URL of the repository
```
Navigate to the directory:
```
cd pronunciation_trainer
```

Create a virtual environment in `.venv` and synchronize the repo:
```
rye sync
```
For more details, visit: [Basics - Rye](https://rye-up.com/guide/basics/)

### Start the App 🌟

Launch the app using:
```
rye run python src/pronunciation_trainer/app.py
```

Then, open your browser and visit [http://localhost:7860](http://localhost:7860/) to start practicing!

