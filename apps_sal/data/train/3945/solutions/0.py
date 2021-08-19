def decipher_message(message):
    n = int(len(message) ** 0.5)
    return ''.join((message[i::n] for i in range(n)))
