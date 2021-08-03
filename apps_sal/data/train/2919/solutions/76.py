def encode(message, key):
    k = [int(x) for x in str(key)]
    return [ord(message[x]) - 96 + k[x % len(k)] for x in range(len(message))]
