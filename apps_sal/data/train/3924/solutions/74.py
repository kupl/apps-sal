def reverse_words(text):
    spaces = text.count('  ')
    text = [x[::-1] for x in text.split()]
    return '  '.join(text) if spaces >= 1 else ' '.join(text)
