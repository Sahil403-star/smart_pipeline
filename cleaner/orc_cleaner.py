def fix_ocr(text):
    if not text:
        return text

    replacements = {
        "l": "1",
        "O": "0",
        "S": "5"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text