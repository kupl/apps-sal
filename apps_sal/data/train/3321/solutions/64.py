def evil(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    if count & 1:
        return "It's Odious!"
    else:
        return"It's Evil!"
