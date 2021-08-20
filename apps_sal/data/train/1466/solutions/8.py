(n, q) = list(map(int, input().split()))
l = list(map(int, input().split()))
v = [0 for x in range(n)]
v[0] = l[0]
for j in range(1, n):
    v[j] = v[j - 1] ^ l[j]
for i in range(q):
    k = int(input())
    if k <= n:
        print(v[k - 1])
    else:
        ans = (k - n) % (n + 1) - 1
        if ans == 0:
            print(0)
        elif ans < 0:
            print(v[n - 1])
        else:
            print(v[ans - 1])
