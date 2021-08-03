def decrypt(s):
    for i in range(1, 11):
        n = int(str(i) + s)
        if n // 11 * 11 == n:
            return str(n // 11)
    return 'impossible'
