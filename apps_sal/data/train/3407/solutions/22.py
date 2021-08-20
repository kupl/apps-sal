from itertools import takewhile


def palindrome_chain_length(n):

    def next_palindrome(m):
        while 1:
            yield m
            m = m + int(str(m)[::-1])
    return len(list(takewhile(lambda x: str(x) != str(x)[::-1], next_palindrome(n))))
