T = int(input())
for no in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    d = dict()
    Flag = 0
    for i in range(N):
        if A[i] in d:
            Flag = 1
            break
        else:
            d[A[i]] = 1
    if Flag == 0:
        print('prekrasnyy')
    else:
        print('ne krasivo')
