def palindrome_chain_length(n):
    c = 0
    rn = int(str(n)[::-1])
    while rn != n:
        n += rn
        rn = int(str(n)[::-1])
        c += 1
    return c
