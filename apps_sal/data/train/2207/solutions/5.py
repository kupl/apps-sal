n = int(input())
u, v = [0, 0], [0, 0]
for i in range(n):
    t, x, y = list(map(int, input().split()))
    k = int(t == 1)
    u[k] += x
    v[k] += y
print('LDIEVAED'[u[1] < v[1] :: 2])
print('LDIEVAED'[u[0] < v[0] :: 2])    

