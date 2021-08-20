def is_odd_heavy(a):
    odd = list(filter(lambda x: x & 1, a)) or []
    even = list(filter(lambda x: not x & 1, a))
    return all((all(map(lambda x: x < i, even)) for i in odd)) if odd else False
