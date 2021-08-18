import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, m = list(map(int, readline().split()))

g = [[1] * n for _ in range(n)]
for i in range(n):
    g[i][i] = 0

for _ in range(m):
    a, b = list(map(int, readline().split()))
    g[a - 1][b - 1] = g[b - 1][a - 1] = 0

used = [-1] * n
dp = 1
ok = 1
for i in range(n):
    if used[i] == -1:
        used[i] = 0
        st = [i]
        a = b = 0
        while st:
            v = st.pop()
            c = used[v]
            if c:
                a += 1
            else:
                b += 1
            for k in range(n):
                if g[v][k] == 1:
                    if used[k] == -1:
                        used[k] = 1 - c
                        st.append(k)
                    elif used[k] == c:
                        ok = 0
                        break

        dp = (dp << a) | (dp << b)
        if not ok:
            dp = 0
            break


ans = -1
for i in range(n // 2 + 1):
    if dp >> i & 1:
        ans = i * (i - 1) // 2 + (n - i) * (n - i - 1) // 2

print(ans)
