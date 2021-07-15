def arbitrate(inp, n):
    if "1" not in inp:return inp
    i=inp.index("1")
    return f"{'0'*i}1{(n-i-1)*'0'}"
