def encode(message, key):
    dicti = {}
    code = []
    ans = []
    letters = list(message)
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(alphabet)):
        dict_ = {alphabet[i]: i + 1}
        dicti.update(dict_)
    for letter in letters:
        for k, v in dicti.items():
            if k == letter:
                code.append(v)
    key_list = list(str(key))
    a = len(message) // len(key_list)
    if len(message) > len(key_list):
        key_list = key_list * (a + 1)
    for j in range(len(code)):
        if j < len(message):
            new_code = code[j] + int(key_list[j])
            ans.append(new_code)
        elif j == len(message):
            break
    return ans
