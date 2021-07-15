def contamination(text, char):
    if len(text)==0:
        return ''
    res = ''
    for i in range(len(text)):
        res += text[i].replace(text[i], char)
        
    return res
