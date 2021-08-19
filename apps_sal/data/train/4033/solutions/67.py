def contamination(text, char):
    return ''.join([i.replace(i, char) for i in text])
