# LoRA Interview Assistant

## Goal
Fine-tune a small LLM to convert technical interview questions into short, structured bullet-point answers.

## Output Format Contract
The model MUST:

- Return exactly 3–4 bullet points
- Each bullet ≤ 15 words
- No paragraphs
- No filler text
- No greetings or explanations
- Only concise technical statements

## Evaluation
- 20 fixed test prompts
- Compare base vs fine-tuned outputs
- Metric: human preference win rate
