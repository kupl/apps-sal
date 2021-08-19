from collections import defaultdict


def find(li, n):
    d = {}
    li.sort()
    for i in range(n):
        if li[i] not in d:
            d[li[i]] = 1
        else:
            d[li[i]] += 1
            if d[li[i]] > 2:
                return 'NO'
    ans = []
    for i in d:
        ans.append(i)
        d[i] -= 1
    for i in range(len(li) - 1, -1, -1):
        if d[li[i]] != 0:
            if ans[-1] == li[i]:
                return 'NO'
            x = d[li[i]]
            while x != 0:
                ans.append(li[i])
                x -= 1
                d[li[i]] -= 1
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    ans = find(li, n)
    if ans != 'NO':
        print('YES')
        for j in ans:
            print(j, end=' ')
        print()
    else:
        print(ans)
