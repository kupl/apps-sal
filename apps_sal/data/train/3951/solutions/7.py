def duplicate_count(text):
    text = text.lower()
    return(sum([text.count(c) > 1 for c in set(text)]))

