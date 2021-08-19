def encode(message, key):
    output = []
    i = 0
    key = [int(d) for d in str(key)]
    for char in message:
        n = ord(char) + key[i]
        output.append(n - 96)
        i = (i + 1) % len(key)
    return output
