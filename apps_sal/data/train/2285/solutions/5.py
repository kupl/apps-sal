t = int(input())

for i in range(t):
    n = int(input())
    s = input().rstrip()
    sint = [int(item) for item in s]
    for div in range(10):
        is_ok = True
        ga = []
        gb = []
        a = 0
        b = div
        for i, item in enumerate(sint):
            if item > div:
                if b > item:
                    is_ok = False
                    break
                else:
                    gb.append(i)
                    b = item
            elif item == div:
                if b == div:
                    gb.append(i)
                else:
                    a = item
                    ga.append(i)
            else:
                if a > item:
                    is_ok = False
                    break
                else:
                    ga.append(i)
                    a = item
        if is_ok:
            break
    if is_ok:
        ans = [1] * n
        for item in gb:
            ans[item] = 2
        print("".join([str(item) for item in ans]))
    else:
        print("-")
