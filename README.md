# 🧠 SaaSquatch Lead Intelligence Tool (Caprae AI Challenge)

This project is a **real-time AI-powered lead enrichment and ranking system** built for the **Caprae Capital AI-Readiness Challenge**. It uses the **Hunter.io API** to enrich company names with actual decision-makers and ranks them using a **zero-shot NLP model** based on role importance.

---

## 🎯 Objective

To simulate a practical B2B lead generation workflow that:
- Pulls decision-makers from public data (via Hunter.io),
- Scores them by role (CEO > Manager),
- Outputs a ranked CSV file,
- And displays it in a lightweight Flask web app.

---

## ⚙️ Features

✅ Real-time company-to-contact enrichment using **Hunter.io**  
✅ Verified public emails, roles, and LinkedIn profiles  
✅ Zero-shot role classification using **HuggingFace Transformers** (with **PyTorch**)  
✅ Ranked final output CSV  
✅ Simple UI built in Flask for selecting companies  
✅ Designed for fast, real-world usage within 5 hours  

---

## 🗂️ Project Structure

```

caprae-leadgen-challenge/
├── data/
│   ├── final.csv                # Final ranked leads
│   ├── raw_master.csv           # Input: list of companies
│   └── enriched_leads.csv       # Intermediate enriched leads from Hunter.io
├── templates/
│   ├── index.html               # Web UI: dropdown to choose company
│   └── company.html             # Web UI: table of ranked leads
├── hunter_enrich.py             # Pulls and enriches leads via Hunter.io
├── ranker.py                    # NLP-based role ranking
├── main.py                      # Flask web app
├── rationale.pdf                # 1-page design rationale
├── video.mp4                    # 1-2 min walkthrough video
├── requirements.txt             # Python dependencies
└── README.md                    # This file

````

---

## 🧠 How It Works

1. User selects a company from the dropdown on `/`
2. Company name is passed to `hunter_enrich.py`
3. It pulls employee data using **Hunter.io Domain Search API**
4. The data is cleaned, verified, and saved to `enriched_leads.csv`
5. `ranker.py` uses **facebook/bart-large-mnli** to assign a score based on title (CEO > VP > Manager, etc.)
6. Final ranked leads are saved in `final.csv`
7. Flask displays them in a clean table

---

## 📦 Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

### 2. Set your Hunter.io API key

Open `hunter_enrich.py` and replace the placeholder:

```python
HUNTER_API_KEY = "ecb5835bbc3b87ab717dde93a04a1f5ddf161cef"
```

### 3. Add companies to enrich

Edit `data/raw_master.csv`:

```csv
company
OpenAI
Microsoft
Anthropic
```

---

## 🚀 Run the App

```bash
python main.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)
Select a company → wait 120-150 seconds → see the top leads 🚀
NOTE: During first time it dowload 1.63 GB package
---

## 📊 Sample Output (final.csv)

| name          | email                                     | role     | company | score | linkedin\_url             | verification\_status |
| ------------- | ----------------------------------------- | -------- | ------- | ----- | ------------------------- | -------------------- |
| Sam Altman    | [sam@openai.com](mailto:sam@openai.com)   | CEO      | OpenAI  | 10    | linkedin.com/in/samaltman | valid                |
| Mira Murati   | [mira@openai.com](mailto:mira@openai.com) | CTO      | OpenAI  | 9     | linkedin.com/in/mira      | valid                |
| Research Lead | [lead@openai.com](mailto:lead@openai.com) | Research | OpenAI  | 6     | linkedin.com/in/lead      | risky                |

---

## 🛠 Dependencies

* Flask
* requests
* pandas
* transformers
* torch

Install all with:

```bash
pip install -r requirements.txt
```

---

## 📥 Sample requirements.txt

```txt
Flask
pandas
requests
transformers
torch
```

---

## 📹 Deliverables

| File               | Purpose                     |
| ------------------ | --------------------------- |
| `README.md`        | ✅ Project overview          |
| `rationale.pdf`    | ✅ 1-page explanation        |
| `video.mp4`        | ✅ 1–2 min video walkthrough |
| `main.py`          | Flask app                   |
| `ranker.py`        | Role classifier             |
| `hunter_enrich.py` | Data enrichment pipeline    |
| `data/*.csv`       | Input/output files          |

---

## 🧠 Model Details

| Component       | Model Used                 |
| --------------- | -------------------------- |
| Role Classifier | `facebook/bart-large-mnli` |
| Framework       | PyTorch                    |
| Inference Type  | Zero-shot classification   |

---

## 🌱 Future Improvements

* 🔗 Public LinkedIn scraping (legally & ethically)
* 📥 CRM integrations (HubSpot, Salesforce)
* 🧠 Fine-tuned role classification models
* 📊 Dashboard with filters & visual analytics
* 📨 Automatic email sequences

---

## 👨‍💻 Author

**Mallikarjun Reddy Bardipuram (Sunny)**
Connect on LinkedIn or GitHub

---

## 🛡️ License

MIT License — free for use, improvement, and deployment.

```

---
