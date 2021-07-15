def contamination(text, char):
    x = ''
    for i in text:
        x = x + char
    if text == '' or char == '':
        return ''
    else:
        return x
