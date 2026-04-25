# def extract_field(item, selector):
#     if "::attr(" in selector:
#         tag, attr = selector.split("::attr(")
#         attr = attr.replace(")", "")
#         element = item.select_one(tag)
#         return element[attr] if element else None
#     else:
#         element = item.select_one(selector)
#         return element.text if element else None


# def extract(items, config):
#     data = []

#     for item in items:
#         obj = {}
#         for field, selector in config["fields"].items():
#             obj[field] = extract_field(item, selector)
#         data.append(obj)

#     return data

def extract_field(item, selector):
    if "::attr(" in selector:
        tag, attr = selector.split("::attr(")
        attr = attr.replace(")", "")
        element = item.select_one(tag)
        return element[attr] if element else None
    else:
        element = item.select_one(selector)
        return element.text if element else None


def extract(items, config):
    result = []

    for item in items:
        obj = {}
        for field, selector in config["fields"].items():
            obj[field] = extract_field(item, selector)
        result.append(obj)

    return result