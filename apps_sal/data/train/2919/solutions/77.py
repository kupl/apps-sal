def encode(message, key):
    a = []
    j = 0
    for i in message:
        a.append(ord(i) - 96 + int(str(key)[j]))
        j += 1
        if j == len(str(key)):
            j = 0
    return a
