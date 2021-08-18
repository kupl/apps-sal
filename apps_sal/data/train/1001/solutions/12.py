
from collections import(deque)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = deque()
    ma = 100000000
    ans = 0
    for i in range(5):
        while d and a[d[0]] > a[i]:
            d.popleft()
        while d and a[d[-1]] > a[i]:
            d.pop()
        d.append(i)
        if a[i] < ma:
            ma = a[i]
            ans += 1
    for i in range(5, len(a)):
        if a[i] < a[d[0]]:
            ans += 1
        while d and a[d[0]] > a[i]:
            d.popleft()
        while d and a[d[-1]] > a[i]:
            d.pop()
        d.append(i)
        if i - d[0] == 5:
            d.popleft()
    print(ans)
