def generate_pairs(n):
    b= [[y,x] for x in range(n+1) for y in range(x+1)]
    b.sort()
    return b
