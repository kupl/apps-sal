def is_palindrome(n):
    return str(n) == str(n)[::-1]


def palindrome_chain_length(n):
    steps = 0
    while not is_palindrome(n):
        steps += 1
        n += int(str(n)[::-1])
    return steps
