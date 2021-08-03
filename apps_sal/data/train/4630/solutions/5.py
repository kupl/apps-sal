def decrypt(s):
    for i in range(1, 11):
        if int(int(str(i) + s)) % 11 == 0:
            return str(int(str(i) + s) // 11)
    return 'impossible'
