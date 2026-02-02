import re

INPUT_FILE = "results/comparison.txt"

def score_answer(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    words = len(text.split())

    bullet_lines = sum(l.startswith(("•", "-", "*")) for l in lines)

    has_bullets = bullet_lines >= 2
    concise = words <= 60
    structured = 2 <= len(lines) <= 6

    return has_bullets, concise, structured


baseline_scores = []
finetuned_scores = []

with open(INPUT_FILE, encoding="utf-8") as f:
    content = f.read().split("============================================================")

for block in content:
    if "BASELINE:" not in block:
        continue

    base = re.search(r"BASELINE:\n(.*?)\n\nFINETUNED:", block, re.S)
    ft = re.search(r"FINETUNED:\n(.*)", block, re.S)

    if not base or not ft:
        continue

    base_ans = base.group(1).strip()
    ft_ans = ft.group(1).strip()

    baseline_scores.append(score_answer(base_ans))
    finetuned_scores.append(score_answer(ft_ans))


def summarize(scores):
    n = len(scores)
    bullets = sum(s[0] for s in scores)
    concise = sum(s[1] for s in scores)
    structured = sum(s[2] for s in scores)

    return {
        "bullet%": round(bullets/n*100, 1),
        "concise%": round(concise/n*100, 1),
        "structured%": round(structured/n*100, 1)
    }


print("Baseline:", summarize(baseline_scores))
print("Finetuned:", summarize(finetuned_scores))
