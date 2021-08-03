MOD = 1000000007
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    # n = int(input())
    weights = list(map(int, input().split()))
    if max(weights) > k:
        print(-1)
    else:
        carry = 0
        rounds = 0
        for w in weights:
            if carry + w <= k:
                carry += w
            else:
                rounds += 1
                carry = w
        if carry > 0:
            rounds += 1
        print(rounds)
