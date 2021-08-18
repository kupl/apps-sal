
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    k = 0
    s = 0
    l1 = [0] * len(l)
    for i in l:
        s = s + i
        l1[k] = s
        k += 1
    b = 1
    day = 0
    while b < n:
        b += l1[b - 1]

        day += 1
    print(day)
