def relevant():
    i = 3
    while True:
        if i % 3 == 0 or i % 5 == 0:
            yield i
        i += 1


def find(n):
    from itertools import takewhile
    return sum(takewhile(lambda x: x <= n, relevant()))
