def multiply(a,b):
    return a if b == 1 else a + multiply(a, b ^ 1) if b & 1 else multiply(a + a, b >> 1) if b else 0
