def evil(n):
    n = bin(n)[2:]
    ans = n.count('1')
    if ans % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
