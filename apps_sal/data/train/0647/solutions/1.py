for t in range(int(input())):
    (n, s) = [int(i) for i in input().split()]
    if n == 1:
        print(s)
        continue
    if s < 2:
        print(-1)
        continue
    if n == 2:
        print(s - 1)
        continue
    l = [0 for i in range(n)]
    s -= 18
    l[0] = 9
    l[-1] = 9
    if s <= 0:
        print(0)
        continue
    res = 1
    for i in range(n):
        temp = min(s, 9 - l[i])
        l[i] += temp
        s -= temp
        res = res * l[i]
        i += 1
    print(res)
