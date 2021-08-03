def iq_test(n):
    n = [int(i) % 2 for i in n.split()]
    if n.count(0) > 1:
        return n.index(1) + 1
    else:
        return n.index(0) + 1
