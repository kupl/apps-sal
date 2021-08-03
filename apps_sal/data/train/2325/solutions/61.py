s = input()
t = input()
n, m = len(s), len(t)
a = [0] * (n + 1)
b = [0] * (m + 1)
for i in range(n):
    a[i + 1] = a[i]
    if s[i] == 'A':
        a[i + 1] += 1
    else:
        a[i + 1] += 2
for i in range(m):
    b[i + 1] = b[i]
    if t[i] == 'A':
        b[i + 1] += 1
    else:
        b[i + 1] += 2
q = int(input())
for _ in range(q):
    i, j, k, l = list(map(int, input().split()))
    if (a[j] - a[i - 1]) % 3 == (b[l] - b[k - 1]) % 3:
        print('YES')
    else:
        print('NO')
