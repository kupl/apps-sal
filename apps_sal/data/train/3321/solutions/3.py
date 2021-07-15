def evil(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return "It's Odious!" if count & 1 else "It's Evil!"
