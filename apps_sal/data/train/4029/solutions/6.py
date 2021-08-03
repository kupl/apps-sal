import re


def search_substr(full_text, search_text, allow_overlap=True):
    if not full_text or not search_text:
        return 0
    if len(search_text) == 1 or not allow_overlap:
        pattern = re.compile(search_text)
    else:
        pattern = re.compile(f"(?<={search_text[:-1]}){search_text[-1]}")
    return len(list(re.findall(pattern, full_text)))
