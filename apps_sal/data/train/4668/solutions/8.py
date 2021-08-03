def is_divisible_by_6(s):
    ls = []
    for x in range(10):
        if int(s.replace("*", str(x))) % 6 == 0:
            ls.append(s.replace("*", str(x)))
    for x in ls:
        if len(x) > 1 and x[0] == "0":
            ls.insert(ls.index(x), x[1:])
            ls.remove(x)
    return ls
