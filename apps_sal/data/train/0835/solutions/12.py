T = int(input())
while T > 0:
    N, M = list(map(int, input().split()))
    if N == 1:
        if M == 2:
            print('Yes')
        else:
            print('No')
    elif M == 1:
        if N == 2:
            print('Yes')
        else:
            print('No')
    elif N % 2 == 1 and M % 2 == 1:
        print('No')
    else:
        print('Yes')
    T = T - 1
