def find_the_key(message, code):
    key = ''.join((str(code[i] + 96 - ord(char)) for (i, char) in enumerate(message)))
    l = len(key)
    for i in range(1, l + 1):
        if (key[:i] * l)[:l] == key:
            return int(key[:i])
