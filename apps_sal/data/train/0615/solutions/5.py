for _ in range(int(input())):
    (N, Q) = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i in range(Q):
        (X, Y) = list(map(int, input().split()))
        print(sum(L[X - 1:Y]))
