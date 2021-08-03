N = int(input())
A = [int(i) for i in input().split()]
B = [[A[i], -10**15] for i in range(2**N)]
for i in range(N):
    for b in range(2**N):
        if ((1 & (b >> i)) == 1):
            merge = B[b] + B[b ^ (1 << i)]
            merge.sort(reverse=True)
            B[b] = merge[:2]
ans = -10**15
for i in range(1, 2**N):
    ans = max([ans, sum(B[i])])
    print(ans)
