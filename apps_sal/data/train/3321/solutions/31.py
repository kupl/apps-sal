def evil(n):
    e = 0
    while n:
        n = n & (n-1)
        e += 1
    return "It's Evil!" if e & 1 == 0 else "It's Odious!"
