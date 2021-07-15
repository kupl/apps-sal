def evil(n):
    return "It's Odious!" if int(str(bin(n))[2:].count('1'))&1 else "It's Evil!"
