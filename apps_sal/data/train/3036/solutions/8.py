def abacaba(k):
    k = k - 1
    for i in range(1, 27):
        if k % 2 ** i == 2 ** (i - 1) - 1:
            return chr(96 + i)
