def reverse_words(text):
    text = text.split(' ')
    return ' '.join([text[i][::-1] for i in range(len(text))])
