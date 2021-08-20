for i in range(0, int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d1 = l[1] - l[0]
    d2 = l[2] - l[1]
    if d2 == d1:
        ce = l[2]
        for j in range(3, n):
            if l[j] == ce + d1:
                ce += d1
            else:
                l[j] = ce + d1
                break
    elif l[3] - l[0] == 3 * d1:
        l[2] = l[1] + d1
    elif l[2] - l[0] == 2 * (l[3] - l[2]):
        l[1] = l[0] + l[3] - l[2]
    else:
        l[0] = 2 * l[1] - l[2]
    for j in range(0, n):
        print(l[j], end=' ')
    print('')
