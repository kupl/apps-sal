def decrypt(s):
    for i in range(1, 11):
        a = int(str(i) + s)
        if a % 11 == 0:
            return str(a // 11)
    return 'impossible'
