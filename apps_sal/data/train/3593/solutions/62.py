def capitalize(s, ind):
    res = []
    for i, char in enumerate(s):
        res += char.upper() if i in ind else char
    return ''.join(res)
