def contamination(text, char):
    return "" if not(text or char) else len(text) * char
