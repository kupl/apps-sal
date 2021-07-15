def sxore(n):
    return (n >> 1) & 1 ^ ( 1 if n&1 else n)

