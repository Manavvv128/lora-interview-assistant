import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from peft import PeftModel

# =========================
# Config
# =========================

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
TEST_FILE = "data/test_prompts.txt"
OUTPUT_FILE = "results/comparison.txt"
ADAPTER_PATH = "model/lora_adapters"   # your saved adapters


# =========================
# Load test prompts
# =========================

with open(TEST_FILE) as f:
    questions = [q.strip() for q in f.readlines()]

print("Questions:", len(questions))


# =========================
# Quantization config
# =========================

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)


# =========================
# Load BASE model
# =========================

print("Loading base model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

base_model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    quantization_config=bnb_config
)

base_pipe = pipeline(
    "text-generation",
    model=base_model,
    tokenizer=tokenizer
)


# =========================
# Load FINETUNED model
# =========================

print("Loading LoRA model...")

ft_model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)

ft_pipe = pipeline(
    "text-generation",
    model=ft_model,
    tokenizer=tokenizer
)


# =========================
# Evaluation
# =========================

results = []

for q in questions:

    prompt = f"Answer briefly using bullet points:\n{q}\n"

    base_out = base_pipe(prompt, max_new_tokens=80, do_sample=False)[0]["generated_text"]
    base_ans = base_out.replace(prompt, "").strip()

    ft_out = ft_pipe(prompt, max_new_tokens=80, do_sample=False)[0]["generated_text"]
    ft_ans = ft_out.replace(prompt, "").strip()

    results.append((q, base_ans, ft_ans))


# =========================
# Save nicely formatted file
# =========================

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for q, b, ft in results:
        f.write(f"Q: {q}\n\n")
        f.write("BASELINE:\n")
        f.write(b + "\n\n")
        f.write("FINETUNED:\n")
        f.write(ft + "\n\n")
        f.write("="*60 + "\n\n")

print("Saved comparison →", OUTPUT_FILE)
