T = int(eval(input()))
for i in range(T):
    n, k = list(map(int, input().split()))
    print(2.0 * (n - 1) * (1 - 1 / k) + 2.0)
