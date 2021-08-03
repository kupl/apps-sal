def encryptor(key, message):
    mod = key % 26
    if mod == 0:
        return message
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    code = []
    for char in message:
        if char.isupper():
            code.append(upper[(upper.find(char) + mod) % 26])
        elif char.islower():
            code.append(lower[(lower.find(char) + mod) % 26])
        else:
            code.append(char)
    return ''.join(code)
