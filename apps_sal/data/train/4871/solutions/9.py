def letter_frequency(text):
    text = text.lower()
    return sorted([(e, text.count(e)) for e in set(text) if e.isalpha()], key=lambda e: (-e[1], e[0]))
