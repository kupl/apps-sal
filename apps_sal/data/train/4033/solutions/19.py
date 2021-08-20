def contamination(text, char):
    a = len(text)
    if type(text) == str:
        return a * char
    if text or char == '':
        return ''
