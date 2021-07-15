def evil(n):
    return "It's Odious!" if int(bin(n).count("1")) % 2 == 1 else "It's Evil!"
