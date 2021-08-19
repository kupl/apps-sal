def reverse_words(text):
    # go for it
    reversed_string = []
    for i in text.split(' '):
        reversed_string.append(i[::-1])
    return ' '.join(reversed_string)
