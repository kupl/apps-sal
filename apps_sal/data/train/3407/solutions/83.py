def is_palindrome(n):
    return str(n) == str(n)[::-1]


def palindrome_chain_length(n):
    c = 0
    while not is_palindrome(n):
        (a, b) = (n, int(str(n)[::-1]))
        n = a + b
        c += 1
    return c
