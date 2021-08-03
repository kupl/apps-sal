def decrypt(s):
    for a in range(1, 11):
        if (a * 10**len(s) + int(s)) % 11 == 0:
            return str((a * 10**len(s) + int(s)) // 11)
    return "impossible"
