from transformers import pipeline

# Use PyTorch backend
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", framework="pt")

# Define role options dynamically or statically
ROLE_OPTIONS = [
    "CEO", "CTO", "Founder", "Engineer", "VP", "Director", "Product Manager",
    "Data Scientist", "Analyst", "Marketing", "Sales", "HR", "Intern"
]

import pandas as pd

def score_roles(input_csv="data/enriched_leads.csv", output_csv="data/final.csv"):
    df = pd.read_csv(input_csv)
    scores = []

    for i, row in df.iterrows():
        description = f"{row['name']} - {row['role']} at {row['company']}"
        result = classifier(description, ROLE_OPTIONS)
        label_scores = dict(zip(result['labels'], result['scores']))
        top_label = result['labels'][0]
        confidence = result['scores'][0]

        scores.append({
            **row,
            "role_detected": top_label,
            "confidence": round(confidence, 4)
        })

    final_df = pd.DataFrame(scores)
    final_df.to_csv(output_csv, index=False)
    print(f"✅ Final ranked leads saved to {output_csv}")

if __name__ == "__main__":
    score_roles()
