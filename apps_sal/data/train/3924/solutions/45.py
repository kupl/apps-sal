def reverse_words(text):
    text = text.split(' ')
    str = ''
    for i in text:
        i = i[::-1]
        str =str + ' '  + i
    return str[1:]

