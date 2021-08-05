n = int(input())

a = []
arr = list(map(int, input().split()))

for i in range(n):
    if len(a) == 0:
        a.append([arr[i]])
        continue
    el = arr[i]
    l, r = 0, len(a) - 1
    while r - l >= 1:
        m = (l + r) // 2
        if el > a[m][-1]:
            r = m
        else:
            l = m + 1
    if el < a[l][-1]:
        a.append([el])
    else:
        a[l].append(el)

for x in a:
    for el in x:
        print(el, end=' ')
    print()
