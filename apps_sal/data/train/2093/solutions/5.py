n = int(input())
lst = list(map(int, input().strip().split()))

ans = [[lst[0]],]
head = [lst[0]]

added = False
for i in range(1, n):
    t = lst[i]
    if (head[len(head)-1]) > t:
        ans.append([t])
        head.append(t)
    else:
        l, r = 0, len(head)-1
        while r-l > 1:
            mm = l + int((r-l)/2)
            if head[mm] < t:
                r = mm
            else:
                l = mm
        if head[l] < t:
            ans[l].append(t)
            head[l] = t
        else:
            ans[r].append(t)
            head[r] = t

for ls in ans:
    print(' ' .join(str(x) for x in ls))
