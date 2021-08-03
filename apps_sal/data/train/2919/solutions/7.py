def encode(message, key):
    a = []
    key = str(key)
    for i in range(len(message)):
        print(i)
        a.append(ord(message[i]) - 96 + int(key[i % len(key)]))
    return a
