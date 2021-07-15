def contamination(text, char):
    nt = len(text)
    nc = len(char)
    if nt == 0 or nc == 0:
        return ""
    return char * nt
