t = "abcdefghijklmnopqrstuvwxyz" * 2
t += t.upper() + "0123456789zzz5678901234"


def ROT135(input):
    return "".join(t[t.index(c) + 13] if c in t else c for c in input)
