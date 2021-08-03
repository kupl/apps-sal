for _ in range(int(input())):
    N = int(input())
    S = str(input())
    P = str(input())
    zero = 0
    one = 0
    ans = True
    for i in range(N):
        if S[i] != P[i]:
            if S[i] == '1':
                one += 1
            else:
                zero += 1
            if one < zero:
                ans = False
                break
    if ans == True and (one == zero):
        print('Yes')
    else:
        print('No')
