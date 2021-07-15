def men_from_boys(arr):
    m = []
    b = []
    for i in arr:
        if i%2==0:
            m.append(i)
            m = list(dict.fromkeys(m))
            m.sort()
        else:
            b.append(i)
            b = list(dict.fromkeys(b))
            b.sort(reverse=True)
    return m + b
