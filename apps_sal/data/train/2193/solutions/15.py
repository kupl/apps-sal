n = int(input())
thomas = sum(map(int, input().split()))
all = [thomas]
for _ in range(n - 1):
    all.append(sum(map(int, input().split())))
all.sort(reverse=True)
i = all.index(thomas)
print(i + 1)

