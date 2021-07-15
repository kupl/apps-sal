def encode(message, key):
    return [ord(message[x])-96+int(str(key)[x%len(str(key))]) for x in range(0,len(message))]
