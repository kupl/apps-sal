def contamination(text, char):
    if text == '':
        return ''
    text = list(text)
    for x in range(len(text)):
        text[x] = char
    return ''.join(text)
