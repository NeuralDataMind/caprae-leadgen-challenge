import requests
import pandas as pd
import time
import argparse

HUNTER_API_KEY = "ecb5835bbc3b87ab717dde93a04a1f5ddf161cef"
HUNTER_DOMAIN_API = "https://api.hunter.io/v2/domain-search"

# Static mapping from company to domain
COMPANY_DOMAIN_MAP = {
    "OpenAI": "openai.com",
    "Google": "google.com",
    "DeepMind": "deepmind.com",
    "Meta": "meta.com",
    "Anthropic": "anthropic.com",
    "Microsoft": "microsoft.com",
    "X":"x.com",
    "Infosys":"infosys.com",
    "TCS": "tcs.com",
    "Caprae Capital":"capraecapital.com"
    # Add more as needed
}

def get_people_from_domain(domain):
    params = {
        "domain": domain,
        "api_key": HUNTER_API_KEY,
        "limit": 20
    }
    response = requests.get(HUNTER_DOMAIN_API, params=params)
    if response.status_code == 200:
        return response.json().get("data", {}).get("emails", [])
    return []

def enrich_from_hunter(input_csv="data/raw_master.csv", output_csv="data/enriched_leads.csv"):
    df = pd.read_csv(input_csv)
    leads = []

    for _, row in df.iterrows():
        company = row["company"]
        domain = COMPANY_DOMAIN_MAP.get(company)

        if not domain:
            print(f"❌ No domain found for {company}")
            continue

        people = get_people_from_domain(domain)
        for person in people:
            first = person.get("first_name") or ""
            last = person.get("last_name") or ""
            name = f"{first.strip()} {last.strip()}".strip()

            leads.append({
                "name": name,
                "email": person.get("value", ""),
                "company": company,
                "role": person.get("position", ""),
                "linkedin_url": person.get("linkedin", ""),
                "verification_status": person.get("verification", {}).get("status", ""),
                "domain_type": "business"
            })

        time.sleep(1.5)  # Rate limit protection

    if leads:
        enriched_df = pd.DataFrame(leads)
        enriched_df.to_csv(output_csv, index=False)
        print(f"✅ Hunter-enriched leads saved to {output_csv}")
        return True
    else:
        print("⚠️ No leads found.")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enrich company data from Hunter.io')
    parser.add_argument('--input', default='data/raw_master.csv', help='Input CSV file path')
    parser.add_argument('--output', default='data/enriched_leads.csv', help='Output CSV file path')
    args = parser.parse_args()
    
    enrich_from_hunter(input_csv=args.input, output_csv=args.output)