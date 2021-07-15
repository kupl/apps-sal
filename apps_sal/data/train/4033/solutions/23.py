def contamination(text, char):
    result = ''
    if (len(text) == 0 or char == ''):
        return ''
    else:
        for x in text:
            result = result + char
    return result
