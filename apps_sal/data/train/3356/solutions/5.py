def three_amigos(a):
    li = []
    for i in range(len(a) - 2):
        s = a[i] & 1
        t = a[i:i + 3]
        if all((j & 1 == s for j in t)):
            m = max(t)
            m_ = min(t)
            li.append([m - m_, t])
    return min(li, key=lambda x: x[0], default=[[], []])[1]
