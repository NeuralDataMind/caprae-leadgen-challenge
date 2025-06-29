# SaaSquatch Lead Intelligence Tool (Caprae AI Challenge)

This project is a streamlined lead scoring and ranking tool inspired by SaaSquatch Leads, built as part of Caprae Capital's AI-Readiness Pre-Screening Challenge.

---

## 📌 Objective

The goal of this project is to simulate how an AI-enhanced lead generation system can help prioritize valuable business contacts based on role relevance, email validity, and company signals.

---

## 💡 Features

* ✅ Company-based lead filtering
* ✅ Email verification and enrichment pipeline
* ✅ Role detection based on title and email patterns
* ✅ Lead scoring using weighted business logic
* ✅ Rank-ordered CSV output (`final.csv`)
* ✅ Bootstrap-powered frontend interface

---

## 📂 Folder Structure

```
caprae-leadgen-challenge/
├── data/
│   ├── final.csv
│   ├── raw_leads.csv
│   ├── raw_master.csv
│   ├── verified_leads.csv
│   └── enriched_leads.csv
├── templates/
│   ├── index.html
│   └── company.html
├── verifier.py
├── enrich_leads.py
├── ranker.py
├── main.py
├── video.mp4
├── rationale.pdf
├── requirements.txt
└── README.md
```

---

## 💧 Tech Stack

* Python (pandas, subprocess)
* Flask (optional for frontend routing)
* Bootstrap (CDN-based styling)
* CSV for I/O

---

## 🚀 How It Works

1. **User selects a company** from dropdown in `index.html`
2. **Company name is injected** into `raw_leads.csv`
3. **`main.py` triggers**:

   * `verifier.py` (email validation)
   * `enrich_leads.py` (industry, size, role detection)
   * `ranker.py` (lead scoring and CSV output)
4. **Results** are displayed from `final.csv` on `company.html`

---

## 📆 Setup & Run

### Requirements

```bash
pip install -r requirements.txt
```

### Run the Pipeline

```bash
python main.py
```

---

## 📄 Deliverables

* `README.md` (you are here)
* `rationale.pdf` (explains business use-case thinking)
* `main.py` (runs full backend pipeline)
* `templates/index.html`, `company.html` (frontend)
* `data/raw_leads.csv` (sample input)
* `video.mp4` (submitted )

---

## 📖 Author

**Mallikarjun Reddy Bardipuram(Sunny)**

---

Your current **🚀 Future Improvements** section is great, but here’s a more polished and expanded version that balances ambition with clarity and aligns even more with Caprae’s expectations:

---

## 🚀 Future Improvements

* **🔗 LinkedIn Profile Scraping (Live):** Automate extraction of public titles, summaries, and activity to enhance role accuracy and enrich metadata.
* **🧠 Role Detection via NLP:** Use transformer-based models (like BERT or DistilBERT) to classify job roles from raw text instead of keyword heuristics.
* **🧩 CRM Integration:** Enable seamless push to Salesforce, HubSpot, or via **Zapier** for immediate lead flow into sales funnels.
* **📈 Behavioral Lead Scoring:** Track website interactions like email opens, page visits, or calendar clicks to enrich the lead score dynamically.
* **🔍 Smart Filtering & Search:** Let users filter leads by department, seniority, email type, or past interactions with customizable flags.
* **📬 Automated Follow-Ups:** Integrate with tools like Mailchimp or Apollo to trigger email cadences based on lead rank and type.
* **🔒 Ethical Data Handling:** Add GDPR-compliant consent flags and scraping safeguards to ensure regulatory alignment.
* **🌐 Browser Extension:** Create a Chrome extension to tag leads from LinkedIn or Crunchbase in real time.
* **📊 Analytics Dashboard:** Build a dashboard to track outreach efficiency, lead conversion, and ICP (ideal customer profile) alignment.

---
