from collections import Counter
n = int(input())
a = map(int, input().split())
b = Counter(a).values()
maxx = max(b)
print(n - maxx)
