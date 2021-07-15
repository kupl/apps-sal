def contamination(text, char):
    return char*(len(text) if char and text else 0)
