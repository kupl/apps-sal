def decrypt(s):
    for i in range(1, 100):
        n = int(str(i) + s)
        if n % 11 == 0 and len(str(n // 11)) == len(s):
            return str(n // 11)
    return 'impossible'
