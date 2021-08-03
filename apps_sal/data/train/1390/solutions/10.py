for _ in range(int(input())):
    N, Q = map(int, input().split())
    ans = (Q * (N + Q + 1) / (Q + 1))
    print(f'{ans:.10f}')
