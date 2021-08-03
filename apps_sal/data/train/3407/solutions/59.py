def is_palindrome(n):
    return str(n) == str(n)[::-1]


def palindrome_chain_length(n):
    if is_palindrome(n):
        return 0
    step = 0
    while not is_palindrome(n):
        rev = int(str(n)[::-1])
        n = n + rev
        step += 1
    return step
