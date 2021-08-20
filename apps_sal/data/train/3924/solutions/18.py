def reverse_words(text):
    return ' '.join((e[::-1] for e in text.split(' ')))
