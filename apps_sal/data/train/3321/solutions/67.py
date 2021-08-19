def evil(n):
    print(bin(n))
    return "It's Evil!" if bin(n).count('1') % 2 == 0 else "It's Odious!"
