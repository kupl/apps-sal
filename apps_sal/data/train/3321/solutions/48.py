def evil(n):
    return "It's Evil!" if sum([1 for i in bin(n) if i == '1']) % 2 == 0 else "It's Odious!"
