def encode(message, key):
    key = list(str(key))
    alpha = list('0abcdefghijklmnopqrstuvwxyz')
    message = list(message)
    code = [alpha.index(message[i]) for i in range(len(message)) if message[i] in alpha]
    i = -1
    for j in range(len(code)):
        if i == len(key) - 1:
            i = -1
        i += 1
        code[j] = code[j] + int(key[i])
    return code
