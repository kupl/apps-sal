from collections import Counter
val = int(input())
for i in range(val):
    n = input()
    n = int(n)
    p = list(map(int, input().split()))
    c = Counter(p)
    print(n - max(c.values()))
