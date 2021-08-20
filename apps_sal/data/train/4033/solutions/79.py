def contamination(text, char):
    return ''.join((char for i in range(len(text)))) if len(text) > 0 or len(char) > 0 else ''
