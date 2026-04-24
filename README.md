# 🚀 Smart Data Extraction & Cleaning Pipeline

A modular, config-driven data extraction pipeline built using Python to scrape, clean, and transform structured data from inconsistent web sources.

---

## 📌 Overview

This project simulates a real-world data engineering workflow by extracting data from web pages, handling inconsistent formats, and converting them into structured datasets.

It focuses on:
- Handling messy and unstructured data
- Building scalable data pipelines
- Applying real-world data cleaning techniques

---

## ✨ Features

- 🔧 **Config-Driven Extraction**
  - Uses JSON-based selectors for dynamic data extraction

- 🧹 **Regex-Based Cleaning**
  - Cleans and normalizes inconsistent formats like prices

- 🤖 **OCR Noise Handling**
  - Fixes common OCR errors (e.g., `l → 1`, `O → 0`)

- ⚙️ **Rule Engine**
  - Applies validation rules to ensure clean and reliable data

- 📦 **Modular Architecture**
  - Separate modules for scraping, extraction, cleaning, and pipeline

- 🖥️ **CLI Support**
  - Run the pipeline with custom parameters

---

## 🏗️ Project Structure

smart_pipeline/
│
├── scraper/ # Web scraping logic
├── extractor/ # Config-based extraction
├── cleaner/ # Regex + OCR cleaning
├── rules/ # Validation rules
├── pipeline/ # Pipeline orchestration
├── config/ # JSON configs
├── data/ # Output files
├── main.py # CLI entry point
├── requirements.txt
└── README.md

---

## ⚙️ Installation

```bash
git clone https://github.com/Sahil403-star/smart_pipeline.git
cd smart_pipeline

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```bash

## ▶️ Usage

Run the pipeline using CLI:

```bash
python main.py --pages 3
```bash

📊 Output

The pipeline generates:

data/output.csv
data/output.json

Example output:

[
  {
    "title": "Sample Book",
    "price": 51.77
  }
]

🧠 Key Learnings
Handling inconsistent and unstructured data
Using regex for data cleaning
Designing modular data pipelines
Config-driven system design
Building CLI-based tools

🚀 Future Improvements
Multi-source scraping (multiple websites)
Email/receipt parsing using XPath
Database integration (SQL/NoSQL)
Data visualization dashboard

👨‍💻 Author

Sahil

📌 Note

This project demonstrates real-world data extraction challenges similar to industry use cases such as OCR-based receipt parsing and automated data processing systems.
