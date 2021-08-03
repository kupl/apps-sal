n = int(input())
l = list(map(int, input().split()))
c = 1
ans = 0
vis = [0] * 1000005
for i in range(n):
    p = i
    vis[i + 1] = 1
    while vis[l[p]] != 1:
        ans -= -1
        vis[l[p]] = 1
        p = l[p] - 1
if 3 * n % 2 == ans % 2:
    print("Petr")
else:
    print("Um_nik")
