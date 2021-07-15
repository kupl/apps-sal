def encode(message, key):
    mess = list(map(lambda x: ord(x)-96, message))
    str_key = [int(i) for i in str(key)]
    for i in range(0, len(mess)):
        mess[i] = mess[i] + str_key[i % len(str_key)]
    
    return mess
