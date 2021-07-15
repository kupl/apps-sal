def contamination(text, char):
    list = []
    if len(text) == 0 or len(char) == 0:
        return ''
    else:
        for elem in text:
            elem = char
            list.append(elem)
        return ''.join(list)
