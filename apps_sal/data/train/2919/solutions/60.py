def encode(message, key):
    message = [ord(x) - 96 for x in message]
    key = str(key)
    key_list = list(key)
    x = list(key)
    while len(key_list) != len(message):
        if not x:
            x = list(key)
        key_list.append(x.pop(0))
    return [message[i] + int(x) for (i, x) in enumerate(key_list)]
