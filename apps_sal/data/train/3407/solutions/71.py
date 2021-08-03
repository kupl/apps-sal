def palindrome_chain_length(n):
    c, x = 0, n
    while str(x) != str(x)[::-1]:
        x = x + int(str(x)[::-1])
        c = c + 1
    return c
