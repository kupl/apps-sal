def palindrome_chain_length(n):
    a = n
    r = 0
    while a != int(str(a)[::-1]):
        a += int(str(a)[::-1])
        r += 1
    return r
