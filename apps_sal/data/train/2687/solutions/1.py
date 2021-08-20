def format_words(words):
    if not words:
        return ''
    words = [word for word in words if word]
    number_of_words = len(words)
    if number_of_words <= 2:
        joiner = ' and ' if number_of_words == 2 else ''
        return joiner.join(words)
    return ', '.join(words[:-1]) + ' and ' + words[-1]
