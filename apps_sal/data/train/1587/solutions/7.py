for t in range(1):
    r = int(input())
    x = []
    for a in range(1, 200):
        for b in range(a, 200):
            for c in range(b, 200):
                if c >= a + b:
                    break
                else:
                    s = (a + b + c) / 2.0
                    A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                    if abs(A / s - r) < 1e-07:
                        x.append((a, b, c))
    print(len(x))
    for (a, b, c) in x:
        print(a, b, c)
