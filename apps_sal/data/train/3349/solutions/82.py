def find_missing_number(s):
    try:
        l = sorted([int(i) for i in s.split()])
    except:
        return 1
    if l == []:
        return 0
    a = [i for (i, x) in enumerate(l, min(l))]
    b = [x for (i, x) in enumerate(l, min(l))]
    if a == b and a[0] == 1:
        return 0
    c = [i for (i, x) in enumerate(l, 1)]
    d = [x for (i, x) in enumerate(l)]
    return min([i for i in c if i not in d])
