for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().strip().split()))
    c = 0
    for i in range(N):
        if A[i] & 1:
            continue
        else:
            c = 1
            break
    if c == 0:
        print('YES')
    else:
        print('NO')
