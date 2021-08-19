mod = 10 ** 9
mod += 7
t = input()
t = int(t)
while t > 0:
    z = input()
    (N, K) = z.split(' ')
    N = int(N)
    K = int(K)
    t -= 1
    if N == 1:
        print(K)
    elif K == 1:
        print(0)
    elif K == 2:
        print(2)
    else:
        res = pow(K - 1, N - 1, mod)
        res *= K
        res %= mod
        print(res)
