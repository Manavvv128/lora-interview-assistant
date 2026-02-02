
# LoRA Fine-Tuned Interview Assistant (TinyLlama)

A parameter-efficient fine-tuning project that adapts a small Large Language Model to produce concise, structured bullet-point answers for technical interview questions.

Instead of retraining the full model, this project uses LoRA (Low-Rank Adaptation) with 4-bit quantization, enabling fast training on limited GPU resources.

---

## Problem

Base LLMs tend to:
- generate long paragraphs
- be verbose
- lack structure

For interview-style responses, we want:
- short answers
- bullet points
- concise explanations
- consistent formatting

---

## Solution

Fine-tuned a 1.1B parameter model using:

- LoRA (parameter-efficient fine-tuning)
- 4-bit quantization (bitsandbytes)
- ~150 curated training samples
- automated evaluation pipeline

Base model:
TinyLlama-1.1B

---


## Results (Quantitative)

| Metric | Baseline | Fine-tuned |
|--------|----------|-----------|
| Bullet format compliance | 0% | 95% |
| Concise answers | 50% | 100% |
| Structured style | 80% | 80% |

Key takeaway:
Fine-tuning improved structured bullet formatting from 0% → 95% while reducing verbosity to 100% concise answers.

---

## Example Output

Before (baseline):
Gradient descent is a popular optimization algorithm used for solving...

After (fine-tuned):
• Minimizes loss function
• Updates weights iteratively
• Moves opposite gradient
• Converges to optimum

---

## How to Run

Install:
pip install -r requirements.txt

Evaluate:
python scripts/evaluate.py

Score metrics:
python scripts/score_results.py

---

## Tech Stack

- Python
- Transformers
- PEFT (LoRA)
- BitsAndBytes
- PyTorch
- Google Colab

---

## Key Learnings

- Parameter-efficient fine-tuning with LoRA
- Memory optimization via quantization
- Dataset design for behavioral control
- Automated evaluation pipelines
- Reproducible ML experiments

---

## Author

Manav Taparia
AI/ML Enthusiast | Python Developer



