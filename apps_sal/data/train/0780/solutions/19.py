T = eval(input())
for t in range(T):
    N, M = list(map(int, input().strip().split()))
    print('EVEN' if (N % M) % 2 == 0 else 'ODD')
