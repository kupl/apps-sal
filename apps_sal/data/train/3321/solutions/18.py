def evil(a):
    return "It's Odious!" if str(bin(a)).count('1') % 2 == 1 else "It's Evil!"

