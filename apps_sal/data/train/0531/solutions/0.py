# cook your dish here
n = int(input())
counts = dict()
z = 0
upper = None
for i in range(0, n):
    a, h = [int(num) for num in input().split()]
    counts[a] = h
for key, count in counts.items():
    c = 0
    x = key - count
    y = key + count
    c1 = 0
    c2 = 0
    for j in counts.keys():
        if j == key:
            continue
        else:
            if x <= j <= key:
                c1 = 0
                break
            else:
                c1 = 1
    for j in counts.keys():
        if j == key:
            continue
        else:
            if key <= j <= y:
                c2 = 0
                break
            else:
                c2 = 1
    if c2 == 0 and c1 == 1:
        if upper is None:
            z = z + c1
            upper = key
        else:
            if x >= upper:
                z = z + c1
                upper = key
            else:
                z = z + c2
                upper = key
    elif c2 == 1 and c1 == 0:
        if upper is None:
            z = z + c2
            upper = y
        else:
            if upper <= key:
                z = z + c2
                upper = y
            else:
                z = z + c1
                upper = y
    elif c2 == 1 and c1 == 1:
        if upper is None:
            z = z + c1
            upper = key
        else:
            if x >= upper:
                z = z + c1
                upper = key
            else:
                if upper <= key:
                    z = z + c2
                    upper = y
                else:
                    z = z + 0
                    upper = y
    else:
        z = z + 0
        upper = key
if len(counts) == 1:
    print(1)
else:
    print(z)
