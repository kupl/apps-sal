def contamination(text, char):

    if not (text or char):
        return ''
    return char * len(text)
