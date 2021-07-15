def palindrome_chain_length(n):
    c = 0
    rev = int(str(n)[::-1])
    while n != rev:
        n = n + rev
        rev = int(str(n)[::-1])
        c += 1
    return c
