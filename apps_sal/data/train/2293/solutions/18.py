N = int(input())
A = list(map(int, input().split()))
 
#dp[S] = A[S], -inf で初期化　Sの部分集合TのうちA[T]が(最大のもの, 次に大きいもの)　を入れていく
 
dp = [[A[S], -float('inf') ] for S in range(1 << N)]
for i in range(N):
    for T in range( 1 << N):
        if (T >> i) & 1 == 1: # Tがiを含むとき
            merge = dp[T] + dp[T ^ (1 << i)]
            merge.sort(reverse = True)
            dp[T] =merge[:2]
ans = -float('inf')
for S in range(1, 1 << N , 1):
    ans = max(ans, sum(dp[S]))
    print(ans)
