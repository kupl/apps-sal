def encode(message, key):
    arr = []
    for i in range(len(message)):
        arr.append(ord(message[i]) - 96 + int(str(key)[i % len(str(key))]))
    return arr
    

