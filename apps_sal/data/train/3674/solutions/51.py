def add_binary(a, b):
    string = bin(a + b)
    return string.replace('0b', '')
