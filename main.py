from flask import Flask, render_template, request
import pandas as pd
import subprocess
import os

app = Flask(__name__)

# Load available companies from master list (for dropdown)
master = pd.read_csv("data/raw_master.csv")
available_companies = sorted(master["company"].dropna().unique())

@app.route('/')
def index():
    return render_template("index.html", companies=available_companies)

@app.route('/company', methods=['POST'])
def process_company():
    selected_company = request.form['company']

    # Filter the master data for the selected company only
    master = pd.read_csv("data/raw_master.csv")
    filtered_df = master[master["company"] == selected_company]
    
    # Create a temporary file for processing
    temp_input = "data/temp_selected_company.csv"
    filtered_df.to_csv(temp_input, index=False)

    # Run enrichment and ranking pipeline
    try:
        subprocess.run(["python", "hunter_enrich.py", "--input", temp_input])
        subprocess.run(["python", "ranker.py"])
        
        # Load final ranked leads
        final_df = pd.read_csv("data/final.csv")
        leads = final_df.to_dict(orient="records")
        
        return render_template("company.html", company=selected_company, leads=leads)
    finally:
        # Clean up temporary file
        if os.path.exists(temp_input):
            os.remove(temp_input)

if __name__ == "__main__":
    app.run(debug=True)