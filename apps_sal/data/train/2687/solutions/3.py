def format_words(words):
    return " and ".join(", ".join(filter(bool, words or [])).rsplit(", ", 1))
