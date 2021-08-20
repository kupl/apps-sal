n = int(input())
strength = list(map(int, input().split()))
sum = 0
i = 0
while i < n - 1:
    j = i + 1
    while j < n:
        sum = sum + abs(strength[i] - strength[j])
        j += 1
    i += 1
print(sum)
