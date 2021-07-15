def evil(n):
    n = str(bin(n))
    b = n.replace('0b', '')
    b = int(b)
    d = [int(i) for i in str(b)]
    if d.count(1) % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"

