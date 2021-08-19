def palindrome_chain_length(n):
    return 0 if str(n) == str(n)[::-1] else (lambda l: ([None for i in iter(lambda: (([None for l[1] in [l[1] + int(str(l[1])[::-1])]], [None for l[0] in [l[0] + 1]]), str(l[1])[::-1] != str(l[1]))[1], False)], l[0])[1])({0: 0, 1: n})
