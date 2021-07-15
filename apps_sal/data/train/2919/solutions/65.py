def encode(message, key):
    key = str(key)
    output = []
    for i in range(0, len(message)):
        output.append( ord(message[i]) - 96 + int(key[i%len(key)]) )
    return output
