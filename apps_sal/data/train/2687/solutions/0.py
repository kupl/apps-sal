def format_words(words):
    return ', '.join((word for word in words if word))[::-1].replace(',', 'dna ', 1)[::-1] if words else ''
