
n, m = map(int, input().split())
buf = []
for i in range(n // 2):
    for j in range(m):
        buf.append(f'{i + 1} {j + 1}\n')
        buf.append(f'{n - i} {m - j}\n')

if n % 2 == 1:
    for j in range(m // 2):
        buf.append(f'{n // 2 + 1} {j + 1}\n')
        buf.append(f'{n // 2 + 1} {m - j}\n')
    if m % 2 == 1:
        buf.append(f'{n//2 + 1} {m//2 + 1}\n')
print(*buf, sep='')
