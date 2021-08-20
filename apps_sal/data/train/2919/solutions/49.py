def encode(message, key):
    num = []
    key = str(key)
    length = len(key)
    for i in range(0, len(message)):
        num.append(ord(message[i]) - 96 + (ord(key[i % length]) - 48))
    print(num)
    return num
