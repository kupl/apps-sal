def palindrome_chain_length(n, cr=0):
    while str(n) != str(n)[::-1]:
        (n, cr) = (n + int(str(n)[::-1]), cr + 1)
    return cr
