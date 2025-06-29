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

**Mallikarjun (Sunny)**

---

## 🚀 Future Improvements

* Live LinkedIn profile scraping
* Real-time role classification using NLP
* CRM integration / Zapier export
* Lead funnel scoring via website behavior

---
