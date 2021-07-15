def encode(message, key):
    return [ord(j)-96+int((str(key)*(len(message)//len(str(key))+1))[i]) for i, j in enumerate(message)]
