def encode(message, key):
    val = [ord(i) - 96 for i in message]
    check = str(key)
    index = 0
    for (idx, i) in enumerate(val):
        if idx % len(check) == 0:
            index = 0
        val[idx] += int(check[index])
        index += 1
    return val
