
import bisect

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    total = sum(a)
    diff = {}
    inter_sum = 0
    for i in range(n - 1):
        if(a[i] == 0):
            continue
        inter_sum += a[i]
        c = inter_sum - (total - inter_sum)
        if(c in list(diff.keys())):
            diff[c].append(i)
        else:
            diff[c] = [i]
    count = 0
    for i in range(n):
        if(-a[i] in list(diff.keys())):
            ans = bisect.bisect_left(diff[-a[i]], i)

            count += ans
        if(a[i] in list(diff.keys())):
            ans = bisect.bisect_left(diff[a[i]], i)
            count += (len(diff[a[i]]) - ans)
    print(count)
