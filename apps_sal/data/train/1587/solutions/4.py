R = int(input())
t = []
for a in range(2 * R, 50):
    for b in range(a, 500):
        for c in range(b, 500):
            s = (a + b + c) / 2.0
            d = s * (s - a) * (s - b) * (s - c)
            if d >= 0 and s != 0 and (a + b > c):
                if R ** 2 == d / s ** 2:
                    t.append([a, b, c])
                    if len(t) > 20:
                        break
print(len(t))
for i in range(len(t)):
    print(t[i][0], t[i][1], t[i][2])
