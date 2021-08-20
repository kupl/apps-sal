from collections import Counter
nos_sweet = int(input())
sweet_types = Counter([int(x) for x in input().split()])
days = 0
for (_, v) in list(sweet_types.items()):
    (d, r) = divmod(v, 2)
    days += d + r
print(days)
