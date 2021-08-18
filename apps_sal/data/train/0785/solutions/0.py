a = int(input())
for i in range(a):
    b = int(input())
    li = []
    if b == 2:
        print(2, 1)
    elif b == 3:
        print(3, 2)
    elif b == 4:
        print(4, 2)
    else:
        for t in range(b + 1):
            if ((b * t) + 1 - (2**t)) < 0:
                li.append(t - 1)
                break
        for o in range(b + 1):
            if b <= 2**(o):
                li.append(o)
                break
        print(*li)
