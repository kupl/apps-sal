def contamination(text, char):
    res = ''
    for i in text:
        if text == ' ':
            return text
        else:
            res += char
    return res
