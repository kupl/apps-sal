import bisect

N = int(input())
x = list(map(int, input().split()))
L = int(input())

dest = []
dest_1 = [0] * N
for i in range(N):
    dest_1[i] = bisect.bisect_left(x, x[i] + L + 0.5) - 1
dest.append(dest_1)
for i in range(1, len(bin(N - 1)) - 1):
    dest_prev = dest[i - 1]
    dest_i = [0] * N
    for j in range(N):
        dest_i[j] = dest_prev[dest_prev[j]]
    dest.append(dest_i)

Q = int(input())
for _ in range(Q):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    k = len(dest) - 1
    ans = 0
    while True:
        d = dest[k][a]
        if d >= b:
            if k > 0:
                k -= 1
            else:
                ans += 1
                break
        else:
            ans += 2 ** k
            a = d
    print(ans)
