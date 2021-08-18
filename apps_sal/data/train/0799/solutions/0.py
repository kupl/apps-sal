n = int(input())
count = 0
for _ in range(n):
    L = list(map(int, input().split()))
    if (L.count(1) >= 2):
        count += 1

print(count)
