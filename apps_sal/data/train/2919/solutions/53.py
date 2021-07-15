def encode(message, key):
    x = [ord(i) - 96 for i in message]
    x = [x[i] + int(str(key)[i % len(str(key))]) for i in range(len(x))]
    return x
