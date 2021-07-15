def contamination(text, char):
    if not char or not text:
        return ""
    else:
        return char * len(text)

