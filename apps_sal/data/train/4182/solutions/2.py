from itertools import count


def survivor(n):
    for i in count(2):
        if i > n:
            return True
        q, r = divmod(n, i)
        if not r:
            return False
        n -= q
