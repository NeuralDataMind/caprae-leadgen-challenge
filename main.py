from flask import Flask, render_template, request
import pandas as pd
import subprocess

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

    # ✅ Load base raw_leads.csv (15 static rows)
    df = pd.read_csv("data/raw_leads.csv")

    # ✅ Replace all values in 'company' column with selected company
    df['company'] = selected_company

    # ✅ Overwrite the file so verifier.py can read it
    df.to_csv("data/raw_leads.csv", index=False)

    # ✅ Run the pipeline
    subprocess.run(["python", "verifier.py"])
    subprocess.run(["python", "enrich_leads.py"])
    subprocess.run(["python", "ranker.py"])

    # ✅ Load and display the final output
    final_df = pd.read_csv("data/final.csv")
    leads = final_df.to_dict(orient="records")

    return render_template("company.html", company=selected_company, leads=leads)

if __name__ == "__main__":
    app.run(debug=True)
