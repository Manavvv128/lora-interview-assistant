import json

questions = [
    "What is gradient descent?",
    "Explain overfitting.",
    "What is regularization?",
    "What is cross validation?",
    "Explain bias vs variance.",
    "What is dropout?",
    "What is backpropagation?",
    "Explain CNN.",
    "What is feature scaling?",
    "What is normalization?",
    "What is standardization?",
    "Explain logistic regression.",
    "What is k-means clustering?",
    "Explain decision trees.",
    "What is random forest?",
    "What is SVM?",
    "Explain precision and recall.",
    "What is F1 score?",
    "What is a confusion matrix?",
    "What is batch size?",
    "What is epoch?",
    "Explain learning rate.",
    "What is early stopping?",
    "What is PCA?",
    "Explain embeddings.",
    "What is tokenization?",
    "What is TF-IDF?",
    "Explain REST API.",
    "What is hashing?",
    "Explain quicksort.",
]

template_answers = [
    [
        "• Core optimization algorithm",
        "• Updates weights iteratively",
        "• Minimizes objective function",
        "• Widely used in ML"
    ],
    [
        "• Improves model generalization",
        "• Reduces overfitting risk",
        "• Controls complexity",
        "• Stabilizes training"
    ],
    [
        "• Splits data into parts",
        "• Trains and validates repeatedly",
        "• Estimates real performance",
        "• Reduces evaluation bias"
    ]
]

output_path = "data/train.jsonl"

with open(output_path, "a", encoding="utf-8") as f:
    for i in range(140):
        q = questions[i % len(questions)]
        ans = template_answers[i % len(template_answers)]
        response = "\n".join(ans)

        item = {
            "instruction": q,
            "response": response
        }

        f.write(json.dumps(item) + "\n")

print("Added 140 samples")
# This script generates a dataset of question-answer pairs for training purposes.