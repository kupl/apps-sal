n = int(input())
data = []
for i in range(n):
    a = [int(v) for v in input().split()]
    data.append((-sum(a), i))
data.sort()
for (j, (_, i)) in enumerate(data):
    if i == 0:
        print(j + 1)
        break
