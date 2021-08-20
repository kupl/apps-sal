T = int(input())
for _ in range(T):
    X = list(map(int, input().split()))
    x = y = 0
    A = (X[0] ** 2 + X[1] ** 2) ** 0.5
    B = (X[2] ** 2 + X[3] ** 2) ** 0.5
    if A > B:
        print('B IS CLOSER')
    else:
        print('A IS CLOSER')
