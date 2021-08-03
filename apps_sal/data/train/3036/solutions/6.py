def abacaba(k):
    for i in range(26):
        if k % (2**(i + 1)) == 2**i:
            return chr(i + 97)
