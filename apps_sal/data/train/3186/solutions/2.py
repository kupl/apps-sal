def similarity(a, b):
    c = a + b
    lst1 = []
    lst2 = []
    for i in set(c):
        if c.count(i) > 1:
            lst1.append(i)
            lst2.append(i)
        else:
            lst2.append(i)
    return len(lst1) / len(lst2)
