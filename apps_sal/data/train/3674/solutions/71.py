def add_binary(a,b):
    out = a + b
    out = bin(out)
    out = out.split("b")
    return out[1]
