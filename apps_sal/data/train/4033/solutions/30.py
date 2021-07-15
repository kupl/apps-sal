def contamination(text, char):
    if text == "" or char == "":
        return ""
    
    res = ""
    for t in text:
        res += char
    return res
