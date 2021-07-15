def palindrome_chain_length(n):
    pal = int(str(n)[::-1])
    res = 0
    while n != pal:
        n += pal
        pal = int(str(n)[::-1])
        res += 1
    return res
