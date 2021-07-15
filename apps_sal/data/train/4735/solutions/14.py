def keep_order(ary, val):
    print(ary, val)
    a = ary
    a.append(val)
    a.sort()
    for i, j in enumerate(a):
        if j == val:
            return i
