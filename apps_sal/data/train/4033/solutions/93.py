def contamination(text, char):
    if not (text or char):
        return ''
    else:
        return char * (len(text))
