def contamination(text, char):
    if text == "":
        return text
    if char == "":
        return char
    else:
        return char * len(text)


