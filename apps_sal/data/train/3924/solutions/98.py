def reverse_words(text):
    textlist = text.split(' ')
    textlist = map(lambda x: x[::-1], textlist)
    return ' '.join(textlist)
