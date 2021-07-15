T = int(input())

for testcase in range(T):
    X, K = list(map(int, input().split(" ")))

    def get_factors(N):
        res = []
        for i in range(2, N+1):
            if N % i == 0:
                res.append(i)
        return res
    
    x_factors = get_factors(X)
    k_factors = get_factors(K)
    
    power_sum = sum([x ** K for x in x_factors])
    factor_sum = sum([k * X for k in k_factors])
    
    print(power_sum, factor_sum)

