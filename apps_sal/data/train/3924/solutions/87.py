def reverse_words(text):
    w = text.split(' ')
    s = ''
    for i in w:
        x = i[::-1]
        if s == '':
            s = x
        else:
            s = s + ' ' + x
    return s
