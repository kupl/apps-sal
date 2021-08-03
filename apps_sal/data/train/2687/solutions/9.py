def format_words(words):
    words = [w for w in words if w] if words else ''
    if not words:
        return ''
    return f'{", ".join(words[:-1])} and {words[-1]}' if len(words) != 1 else words[-1]
