M = 10**9 + 7
n = int(input())
f = list(map(int, input().split()))
q = int(input())
for i in range(q):
    query = input().split()
    if query[0] == '1':
        f[int(query[1]) - 1] = int(query[2])
    else:
        r = int(query[1])
        k = 0
        ans = 1
        while k < n:
            ans *= f[k]
            k += r
        print(str(ans)[0], ans % M)
