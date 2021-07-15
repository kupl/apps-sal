def contamination(text, char):
    if text == '' or char == '':
        return ''
    elif len(text) > 0:
        return len(text)*char

