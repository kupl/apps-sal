def encode(s, k):
    eng = '_abcdefghijklmnopqrstuvwxyz'
    b = list(map(int, list(str(k))))
    q, r = divmod(len(s), len(str(k)))
    return list(map(lambda x, y: x + y, b * q + b[:r], list([eng.index(_) for _ in s])))
