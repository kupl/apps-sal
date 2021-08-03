n = int(input())
a = input()
b = input()

c = [10**10 for i in range(n + 10)]

c[0] = 0 if a[0] == b[0] else 1

for i in range(1, n):
    if a[i] == b[i]:
        c[i] = c[i - 1]
    elif a[i] == b[i - 1] and a[i - 1] == b[i]:
        c[i] = (1 + c[i - 2] if i > 1 else 1)
    c[i] = min(c[i], c[i - 1] + 1)

print(c[n - 1])
