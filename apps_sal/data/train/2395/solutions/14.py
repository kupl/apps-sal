t = int(input())

for _ in range(t):
    n = int(input())

    x = list(map(int, input()))

    a_larger = False

    a = []
    b = []
    for d in x:
        if a_larger:
            a += ["0"]
            b += [str(d)]
        else:
            if d == 0:
                a += ["0"]
                b += ["0"]
            elif d == 1:
                a += ["1"]
                b += ["0"]
                a_larger = True
            else:
                a += ["1"]
                b += ["1"]
    print("".join(a))
    print("".join(b))
