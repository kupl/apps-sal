for t in range(int(input())):
    n = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    s = 0
    for i in range(n):
        s = s + min(A[i], B[i])
    print(s)
