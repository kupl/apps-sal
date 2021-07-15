def reverse_words(text):
    text = text.split(' ')
    text = [x[::-1] for x in text]
    return ' '.join(text)
