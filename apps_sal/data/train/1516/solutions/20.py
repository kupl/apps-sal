MOD = 1000000007
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == 2:
        last_term = k - 1
        first_term = 1
        no_terms = last_term
        ans = (last_term * (last_term + 1)) // 2
        print(ans % MOD)

    else:
        print(1)
