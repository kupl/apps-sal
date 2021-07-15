inverse = 280000002
mod = 1000000007
for _ in range(int(input())):
    N = int(input())
    if N % 2 == 0:
        N = N // 2 + 1
        a = (2 * ((pow(26, N, mod) - 1) * inverse - 1) ) % mod
        print(a)
    else:
        N = N // 2 + 2
        a = (2 * ((pow(26, N, mod) - 1) * inverse - 1)) % mod
        a = (a - pow(26, N - 1, mod)) % mod
        print(a)
