def decode(code, key):
    base_dict = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1, 27):
        base_dict[i] = alpha[i - 1]
    key_extended = []
    count = 0
    for i in range(len(code)):
        try:
            key_extended.append(int(str(key)[count]))
        except IndexError:
            count = 0
            key_extended.append(int(str(key)[count]))
        count += 1
    key_applied = []
    for i in range(len(code)):
        key_applied.append(code[i] - key_extended[i])
    decrypt = ''
    for elt in key_applied:
        decrypt += base_dict[elt]
    return decrypt
