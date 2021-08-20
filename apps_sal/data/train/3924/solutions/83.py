def reverse_words(text):
    backwards = text[::-1].split(' ')
    text = ''
    print(backwards)
    for word in backwards[::-1]:
        text += word
        text += ' '
    return text[:-1]
