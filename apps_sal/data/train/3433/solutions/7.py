def replace_zero(a):
    li1 = []
    for i, j in enumerate(a):
        if j == 0:
            temp = a[:]
            t, t1, li, temp[i] = i, i + 1, [], 1
            while t >= 0 and temp[t] == 1:
                li.append(temp[t])
                t -= 1
            while t1 <= len(a) - 1 and temp[t1] == 1:
                li.append(temp[t1])
                t1 += 1
            li1.append([len(li), i])
    return sorted(li1, key=lambda x: (-x[0], -x[1]))[0][1]
