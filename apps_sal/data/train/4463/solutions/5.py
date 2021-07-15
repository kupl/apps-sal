def get_positions(text):
    for char in text:
        pos = ord(char)
        if pos >= 65 and pos <= 90:
            yield pos - 64
        if pos >= 97 and pos <= 122:
            yield pos - 96

def alphabet_position(text):
    return " ".join((str(char) for char in get_positions(text)))

