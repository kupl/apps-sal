def contamination(text, char):
    return '' if not text else char + contamination(text[1:], char)
