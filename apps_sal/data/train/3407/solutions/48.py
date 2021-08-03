def is_palindrome(n):
    return str(n) == str(n)[::-1]


def palindrome_chain_length(n):
    out = 0
    while not is_palindrome(n):
        out += 1
        n += int(str(n)[::-1])
    return out
