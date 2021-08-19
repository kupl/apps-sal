def palindrome_chain_length(n):

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def rev(n):
        return int(str(n)[::-1])
    steps = 0
    while not is_palindrome(n):
        (n, steps) = (n + rev(n), steps + 1)
    return steps
