def sort_number(a):
    a.sort()
    if a == [1] * len(a):
        del a[-1]
        a.append(2)
        return a
    l = [1]
    a.remove(max(a))
    for i in range(len(a)):
        l.append(a[i])
    return l
