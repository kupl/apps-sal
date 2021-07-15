def contamination(text, char):
    if not text or not char:
        return ''
    else:
        return char * len(text)
