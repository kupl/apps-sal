def reverse_words(text):
    s = ' '.join([i[::-1] for i in text.split(' ')])
    return s

