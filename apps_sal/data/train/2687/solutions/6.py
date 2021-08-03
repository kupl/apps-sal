def format_words(w=None):
    return ', '.join(filter(lambda _: bool(_), w))[::-1].replace(',', 'dna ', 1)[::-1] if w else ''
