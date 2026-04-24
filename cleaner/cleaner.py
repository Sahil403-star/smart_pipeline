import re

def clean_price(text):
    if not text:
        return None

    match = re.search(r"\d+\.?\d*", text.replace(",", ""))
    return float(match.group()) if match else None