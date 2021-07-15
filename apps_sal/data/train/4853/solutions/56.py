def double_char(s):
    l = list(s)
    res = []
    for letter in l:
        res.append(letter)
        res.append(letter)
    return "".join(res)
