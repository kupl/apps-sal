def reverse_words(text):
    reversed_string = []
    for i in text.split(' '):
        reversed_string.append(i[::-1])
    return ' '.join(reversed_string)
