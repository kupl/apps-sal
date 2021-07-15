from string import ascii_lowercase as letters


def encode(string):
    return ''.join(str(letters.find(char)+1) if char in letters else char for char in string.lower())
