n = int(input())
strength = list(map(int, input().split()))
revenue = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        x = abs(strength[i] - strength[j])
        revenue += x
print(revenue)
