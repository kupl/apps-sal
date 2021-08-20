def decrypt(s):
    for n in range(1, 11):
        (res, mod) = divmod(int(str(n) + s), 11)
        if mod == 0:
            return str(res)
    return 'impossible'
