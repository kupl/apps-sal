n = int(input())
t = [list(map(int, input().split())) for q in range(n)]
n += 1
u = [-10000000.0] * n
v = [0] * n
for (i, (j, a)) in list(enumerate(t, 1))[::-1]:
    u[i] = max(u[i], v[i] + a)
    (v[j], u[j]) = (max(v[j] + v[i], u[j] + u[i]), max(v[j] + u[i], u[j] + v[i]))
print(u[1])
