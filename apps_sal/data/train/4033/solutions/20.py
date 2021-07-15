def contamination(text, char):
    x = []
    if text == '' or char == '':
        return ""
    else:
        for i in range(len(text)):
            x.append(char)
    return ''.join(x)
