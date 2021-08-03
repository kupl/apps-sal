T = int(input())
for k in range(T):
    n, x, m = list(map(int, input().split()))
    l1 = [int(i) for i in input().split()]
    l2, l3 = [], []
    for i in range(len(l1)):
        l2.append(0)
        l3.append(0)
    l2[0] = l1[0] % 1000000007
    for i in range(1, len(l1)):
        l2[i] = ((l2[i] % 1000000007) + (l2[i - 1] % 1000000007)) % 1000000007
    if m == 1:
        print(l1[x - 1] % 1000000007)
    elif m == 2:
        print(l2[x - 1])
    else:
        l3[0] = l2[0]
        l3[1] = (l1[1] + ((m) * l1[0]) % 1000000007) % 1000000007
        s = 0
        v = 0
        for i in range(2, x):
            s = l2[i - 1] * (l2[i - 1] - 1) // 2
            v = l3[i - 1] * (l3[i - 1] + 1) // 2
            l3[i] = (v - s) % 1000000007
    print(l3[x - 1])
