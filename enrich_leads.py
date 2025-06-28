# enrich_leads.py

import pandas as pd
import random

# Load verified leads
df = pd.read_csv("data/verified_leads.csv")

# Sample enrichment pools
industries = ["Software", "Healthcare", "Marketing", "Finance", "E-commerce", "Education"]
company_sizes = ["1-10", "11-50", "51-200", "201-500", "500+"]
public_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
decision_keywords = ["ceo", "founder", "cto", "cofounder", "president", "director", "vp", "chief"]

# Enrichment Functions
def generate_industry():
    return random.choice(industries)

def generate_company_size():
    return random.choice(company_sizes)

def generate_founded_year():
    return random.randint(1990, 2022)

def generate_linkedin_url(company_name):
    handle = company_name.lower().replace(" ", "-").replace(",", "")
    return f"https://linkedin.com/company/{handle}"

def detect_role(name, email):
    joined = f"{name.lower()} {email.lower()}"
    return any(keyword in joined for keyword in decision_keywords)

def get_domain_type(email):
    domain = email.split('@')[-1]
    return "public" if domain in public_domains else "business"

def calculate_lead_score(row):
    score = 0
    if row.get("verification_status") == "✅ Valid":
        score += 40
    if row.get("domain_type") == "business":
        score += 20
    if row.get("role_detected") == True:
        score += 20
    if row.get("company_size") in ["51-200", "201-500", "500+"]:
        score += 20
    return min(score, 100)

# Apply enrichments
df["industry"] = df["company"].apply(lambda x: generate_industry())
df["company_size"] = df["company"].apply(lambda x: generate_company_size())
df["founded_year"] = df["company"].apply(lambda x: generate_founded_year())
df["linkedin_url"] = df["company"].apply(generate_linkedin_url)
df["domain_type"] = df["email"].apply(get_domain_type)
df["lead_score"] = df.apply(calculate_lead_score, axis=1)

# Save output
df.to_csv("data/enriched_leads.csv", index=False)
print("✅ Enriched leads saved to data/enriched_leads.csv")
