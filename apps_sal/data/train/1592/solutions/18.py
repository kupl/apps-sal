for _ in range(int(input())):
    s = 0
    l1 = []
    for i in range(int(input())):
        l = list(map(int, input().split()))
        n = l[0]
        l = l[1:]
        if n % 2 == 0:
            s += sum(l[:n // 2])
        else:
            l1.append(l)
    (l2, l3) = ([], [])
    for i in range(len(l1)):
        l2.append(sum(l1[i][:len(l1[i]) // 2]))
        l2.append(sum(l1[i][:len(l1[i]) // 2 + 1]))
        l3.append(l2)
        l2 = []
    l3.sort()
    for i in range(len(l3)):
        if i < len(l3) // 2:
            s += min(l3[i])
        else:
            s += max(l3[i])
    print(s)
