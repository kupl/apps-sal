def capitalize(s, ind):
    res = ''
    for (key, letter) in enumerate(s):
        if key in ind:
            res += letter.upper()
        else:
            res += letter
    return res
