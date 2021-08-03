def encode(message, key):
    arr = []
    for i in range(len(message)):
        encr = ord(message[i]) - 96
        if i > len(str(key)) - 1:
            k = i - len(str(key)) * (i // len(str(key)))
        else:
            k = i
        arr.append(encr + int(str(key)[k]))

    return arr
