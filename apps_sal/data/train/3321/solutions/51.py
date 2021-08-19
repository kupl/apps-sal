def evil(n):
    return "It's Evil!" if sum([int(i) for i in list(bin(n))[2:]]) % 2 == 0 else "It's Odious!"
