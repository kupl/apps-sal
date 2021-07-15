def search(titles: list, term: str):
    import re
    return [title for title in titles if bool(re.search(term, title, re.IGNORECASE))]
