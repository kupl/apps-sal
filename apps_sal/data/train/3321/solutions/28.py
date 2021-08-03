def evil(n):
    return "It's Odious!" if sum(map(int, bin(n)[2:])) & 1 else "It's Evil!"
