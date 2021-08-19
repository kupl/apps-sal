def encode(message, key):
    message = message.lower()
    key = list(str(key))
    message = list(message)
    for i in range(len(message)):
        message[i] = ord(message[i]) - 96 + int(key[i % len(key)])
    return message
