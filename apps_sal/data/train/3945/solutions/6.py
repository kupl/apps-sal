def decipher_message(message):
    if not message:
        return ''
    s = int(len(message) ** 0.5)
    l = [message[i:i + s] for i in range(0, len(message), s)]
    r = []
    for i in range(s):
        r.append(''.join(list(map(lambda x: x[i], l))))
    return ''.join(r)
