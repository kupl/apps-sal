for _ in range(int(input())):
    n1 = int(input())
    l1 = list(map(int, input().split()))
    n2 = int(input())
    l2 = list(map(int, input().split()))
    a = []
    z = []
    for i in range(len(l2)):
        if l2[i] in l1:
            for j in range(len(l1)):
                if l2[i] == l1[j]:
                    a.append(j)
                    z.append(j)
                    z.sort()
    if len(l2) == len(a) and a == z:
        print('Yes')
    else:
        print('No')
