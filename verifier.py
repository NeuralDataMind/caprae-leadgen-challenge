# verifier.py

import pandas as pd

# Load the raw lead data
df = pd.read_csv("data/raw_leads.csv")

# Step 1: Remove duplicate emails
if 'email' not in df.columns:
    raise ValueError("Missing 'email' column in raw_leads.csv")

df = df.drop_duplicates(subset='email')

# Step 2: Define a realistic mock email verification function
def verify_email(email):
    if not isinstance(email, str) or "@" not in email:
        return "❌ Invalid", "unknown"
    
    domain = email.split("@")[1]
    
    if domain.endswith("invalid.com"):
        return "❌ Invalid", "unknown"
    elif domain in ["gmail.com", "yahoo.com", "hotmail.com"]:
        return "✅ Valid", "personal"
    elif domain.endswith((".com", ".org", ".io", ".net", ".co")):
        return "✅ Valid", "business"
    else:
        return "⚠️ Unknown", "unknown"

# Step 3: Apply verification to each email
df[["verification_status", "domain_type"]] = df["email"].apply(
    lambda x: pd.Series(verify_email(x))
)

# Step 4: Save to verified_leads.csv
df.to_csv("data/verified_leads.csv", index=False)

print("✅ Verified leads saved to verified_leads.csv")
