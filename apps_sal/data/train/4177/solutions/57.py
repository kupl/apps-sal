def men_from_boys(arr):
    men = [n for n in arr if n % 2 == 0]
    boys = [n for n in arr if n % 2 != 0]
    m = []
    b = []
    for n in men:
        if n not in m:
            m.append(n)
    for n in boys:
        if n not in b:
            b.append(n)
    m.sort()
    b.sort(reverse=True)
    return m + b
