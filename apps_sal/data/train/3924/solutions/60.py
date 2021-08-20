def reverse_words(text):
    l = [i[::-1] for i in text.split(' ')]
    return ' '.join(l)
