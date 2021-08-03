from collections import defaultdict
t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    dd = defaultdict(list)
    boo = False
    se = set(a)
    for i in range(len(a)):
        if (a[i] in se and a[a[i] - 1] in dd):
            for j in dd[a[a[i] - 1]]:
                if a[i] != j:
                    boo = True
                    break
        if boo:
            break

        dd[a[a[i] - 1]].append(a[i])
    if boo:
        print('Truly Happy')
    else:
        print('Poor Chef')
