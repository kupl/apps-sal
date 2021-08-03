def caeser(message, key):
    return "".join(char_if(c, key) for c in message.upper())


def char_if(char, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alpha[(alpha.index(char) + key) % 26] if char in alpha else char
