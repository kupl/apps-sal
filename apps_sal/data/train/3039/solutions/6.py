harshad = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(2, 17):
    new = []
    for curr in current:
        for d in range(0, 10):
            if int(str(curr) + str(d)) % sum([int(f) for f in str(curr) + str(d)]) == 0:
                new.append(int(str(curr) + str(d)))
    harshad += new
    current = [d for d in new]
harshad = harshad[9:]
t = len(harshad)


def rthn_between(a, b):
    i1 = 0
    i2 = t
    c1 = -1
    c2 = -1
    f = 0
    while i2 - i1 > 1:
        f = (i1 + i2) // 2
        if harshad[f] < a:
            i1 = f
        else:
            i2 = f
    c1 = i2 if harshad[i1] < a else i1
    i1 = 0
    i2 = t
    while i2 - i1 > 1:
        f = (i1 + i2) // 2
        if harshad[f] < b:
            i1 = f
        else:
            i2 = f
    c2 = i2 if harshad[i1] < b else i1
    return [d for d in harshad[c1:c2 + 1] if a <= d <= b]
