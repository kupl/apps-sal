a = ["a","e","i","o","u"]
def encode(st):
    return "".join([str(a.index(c) + 1) if c in a else c for c in st])
def decode(st):
    return "".join([a[int(c)-1] if c.isdigit() else c for c in st])
