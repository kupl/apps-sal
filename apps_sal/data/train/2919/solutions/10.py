def encode(message, key):
    base_dict = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        base_dict[alpha[i]] = i + 1

    key_extended = []
    count = 0
    for i in range(len(message)):
        try:
            key_extended.append(int(str(key)[count]))
        except IndexError:
            count = 0
            key_extended.append(int(str(key)[count]))
        count += 1

    encrypt = []
    for letter in message:
        encrypt.append(base_dict[letter])

    code = []
    for i in range(len(encrypt)):
        code.append(encrypt[i] + key_extended[i])

    return code
