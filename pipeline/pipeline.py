import json
import pandas as pd

from scraper.scraper import scrape_books
from extractor.extractor import extract
from cleaner.cleaner import clean_price
from cleaner.ocr_cleaner import fix_ocr
from rules.rules_engine import apply_rules

def run_pipeline(pages=2):
    config = json.load(open("config/books.json"))

    raw_items = scrape_books(pages)
    extracted = extract(raw_items, config)

    final = []

    for item in extracted:
        item["price"] = clean_price(fix_ocr(item["price"]))
        item = apply_rules(item)

        if item:
            final.append(item)

    df = pd.DataFrame(final)
    df.to_csv("data/output.csv", index=False)
    df.to_json("data/output.json", orient="records", indent=2)