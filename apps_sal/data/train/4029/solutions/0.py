import re

def search_substr(full_text, search_text, allow_overlap=True):
    if not full_text or not search_text: return 0
    return len(re.findall(f'(?=({search_text}))' if allow_overlap else search_text, full_text))
