def evil(n):
    count = 0
    while n > 0:
        if n >> 1 << 1 != n:
            count += 1
        n >>= 1
    if count % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
