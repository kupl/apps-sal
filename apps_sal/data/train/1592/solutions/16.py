for _ in range(int(input())):
    n = int(input())
    (l, l1) = ([], [])
    l3 = []
    s = 0
    for i in range(n):
        l2 = list(map(int, input().split()))
        n = l2[0]
        l2 = l2[1:]
        if n % 2 == 0:
            s += sum(l2[:len(l2) // 2])
        else:
            l.append(sum(l2[:len(l2) // 2]))
            l.append(sum(l2[:len(l2) // 2 + 1]))
            l1.append(l)
            l = []
            l3.append(l1[len(l1) - 1][1] - l1[len(l1) - 1][0])
    for i in range(len(l3)):
        if i < len(l3) // 2:
            t = l3.index(min(l3))
            s += min(l1[t])
            l1.remove(l1[t])
        else:
            t = l3.index(min(l3))
            s += max(l1[t])
            l1.remove(l1[t])
    print(s)
