t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    k = n // 4
    if l[k - 1] != l[k] and l[2 * k - 1] != l[2 * k] and (l[3 * k - 1] != l[3 * k]):
        print(str(l[k]) + ' ' + str(l[2 * k]) + ' ' + str(l[3 * k]))
    else:
        print('-1')
