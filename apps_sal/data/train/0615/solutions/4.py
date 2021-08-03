# cook your dish here
for _ in range(int(input())):
    N, Q = input().split()
    L = list(map(int, input().split()))
    for i in range(int(Q)):
        X, Y = map(int, input().split())
        s = 0
        for i in range(X - 1, Y):
            s += L[i]
        print(s)
