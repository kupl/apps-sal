def contamination(text, char):

    l = len(text)
    r = l * char

    if text == "" or char == "":
        return ""
    else:
        return r
