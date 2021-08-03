s = input()
t = input()
q = int(input())
x = [1 if s[i] == 'B' else 2 for i in range(len(s))]
y = [1 if t[i] == 'B' else 2 for i in range(len(t))]
for i in range(1, len(s)):
    x[i] += x[i - 1]
for i in range(1, len(t)):
    y[i] += y[i - 1]

for i in range(q):
    a, b, c, d = map(int, input().split())
    u = x[b - 1] - (x[a - 2] if 2 <= a else 0)
    v = y[d - 1] - (y[c - 2] if 2 <= c else 0)
    print('YES' if u % 3 == v % 3 else 'NO')
