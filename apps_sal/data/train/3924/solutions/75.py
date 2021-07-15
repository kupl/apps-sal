def reverse_words(text):
    return ' '.join([''.join(list(i)[::-1]) for i in text.split(' ')])

