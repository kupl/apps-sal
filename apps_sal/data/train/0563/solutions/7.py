T = int(input())

for no in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for q in range(Q):
        Q1 = list(map(int, input().split()))
        s = 0
        for i in range(Q1[0] - 1, Q1[1]):
            s += A[i]
        print(s)
