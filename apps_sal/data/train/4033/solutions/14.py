def contamination(text, char):
    return char * len(text) if len(char) > 0 and len(text) > 0 else ''
