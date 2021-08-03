def reverse_words(text):
    text = text.split(' ')
    re = [i[::-1] for i in text]
    return ' '.join(re)
