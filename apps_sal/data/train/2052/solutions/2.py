n, m = list(map(int, input().split()))
l = [0 for i in range(0, n)]
c = [0 for i in range(0, n)]
sol = 0

for i in range(0, m):
    a, b = list(map(int, input().split()))
    l[a - 1] = 1
    c[b - 1] = 1

for i in range(1, n // 2):
    # ma ocup de liniile i si n-i, coloanele la fel
    sol += 4 - (l[i] + c[i] + l[n - i - 1] + c[n - i - 1])

if n % 2 == 1:
    if not l[n // 2] or not c[n // 2]:
        sol += 1

print(sol)
