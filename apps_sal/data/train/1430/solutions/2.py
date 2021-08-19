t = int(input())
for i in range(t):
    (m, l) = list(map(int, input().split()))
    if m == 1:
        print(1)
    else:
        s = (2 + l) * (m // 2)
        if m % 2 != 0:
            s += 1 + 2 * l
        print(s)
