def evil(n):
    a = bin(n)
    b = str(a)
    c = b.count("1")
    if int(c) % 2 == 0: 
        return "It's Evil!"
    if int(c) % 2 != 0:
        return "It's Odious!"

