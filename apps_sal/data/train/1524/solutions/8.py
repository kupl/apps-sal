def power(x, y):
    if y == 0:
        return 1
    else:
        temp_val = power(x, y // 2)
        if y % 2 == 0:
            return temp_val * temp_val % 1000000007
        else:
            return temp_val * temp_val * x % 1000000007


def __starting_point():
    T = int(input())
    for i in range(T):
        (N, K) = list(map(int, input().split()))
        val = K * power(K - 1, N - 1)
        print(val % 1000000007)


__starting_point()
