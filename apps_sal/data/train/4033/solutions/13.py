def contamination(text, char):
    for i in text:
        text = text.replace(i, char)
    return text
