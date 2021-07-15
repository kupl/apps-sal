from string import ascii_lowercase as alphabet


def decode(message):
    return message.translate(str.maketrans(alphabet, alphabet[::-1]))
