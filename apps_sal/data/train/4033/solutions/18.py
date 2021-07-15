def contamination(text, char):
    res = ''
    if text:
        for c in text:
            res += char
        return res
    else:
        return text
