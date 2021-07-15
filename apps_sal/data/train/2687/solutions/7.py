def format_words(words):
    return ', '.join([word for word in words if word] if words else [])[::-1].replace(' ,', ' dna ', 1)[::-1]
