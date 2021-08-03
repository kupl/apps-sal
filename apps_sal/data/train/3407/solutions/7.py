from itertools import takewhile, accumulate, repeat


def palindrome_chain_length(n):
    return len(list(takewhile(lambda x: str(x) != str(x)[::-1], accumulate(repeat(n), lambda m, _: m + int(str(m)[::-1])))))
