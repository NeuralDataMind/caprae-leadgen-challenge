import pandas as pd

ROLE_SCORES = {
    "ceo": 10,
    "chief executive officer": 10,
    "founder": 10,
    "co-founder": 10,
    "cofounder": 10,
    "cto": 9,
    "chief technology officer": 9,
    "chief": 9,
    "president": 9,
    "vice president": 8,
    "vp": 8,
    "director": 7,
    "manager": 6,
    "lead": 5,
    "engineer": 4,
    "analyst": 3,
    "associate": 2,
    "intern": 1,
    "staff": 2,
    "unknown": 2  # Explicit unknown role handling
}

def clean_role_data(role):
    """Convert all False-like values to 'unknown'"""
    if pd.isna(role) or role in [False, 'False', 'false', 'FALSE']:
        return 'unknown'
    return str(role).strip().lower()

def get_role_score(role):
    """Safe role scoring with unknown handling"""
    clean_role = clean_role_data(role)
    for title, score in ROLE_SCORES.items():
        if title in clean_role:
            return score
    return 2  # Default score

def calculate_final_lead_score(row):
    """Calculate score preserving existing values"""
    base_score = row.get('lead_score', 0)
    role_adjustment = min(row.get('role_score', 2) * 3, 30)  # Reduced weight for roles, capped at 30
    return min(base_score + role_adjustment, 100)

def rank_leads(input_csv="data/enriched_leads.csv", output_csv="data/final.csv"):
    """Process leads and output to final.csv"""
    try:
        # Read with explicit role cleaning
        df = pd.read_csv(
            input_csv,
            dtype={'role': 'string'},
            na_values=['False', 'false', 'FALSE', '']
        )
        
        # Clean and score roles
        df['role'] = df['role'].apply(clean_role_data)
        df['role_score'] = df['role'].apply(get_role_score)
        
        # Calculate metrics
        df['lead_score'] = df.apply(calculate_final_lead_score, axis=1)
        df['priority'] = df['lead_score'].apply(
            lambda x: 'High' if x >= 80 else ('Medium' if x >= 50 else 'Low')
        )
        
        # Sort and save
        df.sort_values('lead_score', ascending=False, inplace=True)
        
        # Maintain original columns plus new ones
        output_cols = [col for col in df.columns if not col.startswith('_')]
        df.to_csv(output_csv, index=False, columns=output_cols)
        
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    rank_leads()