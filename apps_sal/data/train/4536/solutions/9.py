def capitals_first(text):
    words = [word for word in text.split() if word[0].isalpha()]
    return ' '.join(sorted(words, key=lambda x: not x[0].isupper()))
