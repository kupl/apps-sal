n = int(input())
a = list(map(int, input().split()))
groups = []
groupTail = []
for elem in a:
    if not groups:
        groups.append([elem])
        groupTail.append(elem)
    else:
        l = 0
        r = len(groups)
        while l <= r:
            m = (l + r) // 2
            if m == len(groups):
                break
            if l == r:
                break
            if groupTail[m] < elem:
                r = m
            else:
                l = m + 1
        if m == len(groups):
            groups.append([elem])
            groupTail.append(elem)
        else:
            groups[m].append(elem)
            groupTail[m] = elem
for line in groups:
    print(' '.join(map(str, line)))
