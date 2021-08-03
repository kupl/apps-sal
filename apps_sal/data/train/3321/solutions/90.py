def evil(n):
    if int(list(bin(n)).count('1')) % 2 != 0:
        print((list(bin(n)), list(bin(n)).count('1')))
        return "It's Odious!"
    else:
        print((list(bin(n))))
        return "It's Evil!"
