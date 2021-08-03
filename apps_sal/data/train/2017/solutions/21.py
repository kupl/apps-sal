n = int(input())
a = list(map(int, input().split()))
sol = 0
for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        if a[i] == a[j]:
            for k in range(j, i + 1, -1):
                a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1
                sol += 1
            break
print(sol)
