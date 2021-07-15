def abacaba(k):
    n = 26
    if k % 2: return 'a'
    while k % pow(2, n) != 0: n -= 1
    return chr(97 + n)
