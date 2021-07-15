def contamination(text, char):
    return '' if text=='' or char=='' else ''.join(char for letter in text)
