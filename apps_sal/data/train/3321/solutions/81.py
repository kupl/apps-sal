def evil(n):
    x = str(bin(n))[2:]
    t = 0
    for i in x:
        if i == '1':
            t += 1
    if t % 2 == 0 and t >= 1:
        return "It's Evil!"
    else:
        return "It's Odious!"
