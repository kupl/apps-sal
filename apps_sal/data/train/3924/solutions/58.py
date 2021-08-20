def reverse_words(text):
    words = text.split(' ')
    new_text = ''
    for word in words:
        new_text += word[::-1]
        if word is not words[-1]:
            new_text += ' '
    return new_text
