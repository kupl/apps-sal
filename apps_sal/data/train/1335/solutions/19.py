n = int(input())
arr = list(map(int, input().split()))
se = set(arr)
c = []
total = 0
for x in se:
    c.append(arr.count(x))
for x in c:
    total += x // 2
    total += x % 2
print(total)
