from collections import Counter
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x = dict(Counter(l))
    m = max(list(x.values()))
    print(n - m)
