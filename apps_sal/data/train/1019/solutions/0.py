for i in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    (l, h) = (0, N - 1)
    flag = 1
    if L[l] != 1 and L[h] != 1:
        flag = 0
    else:
        while l < h:
            if L[l] != L[h] or (L[l + 1] - L[l] != 1 and L[h - 1] - L[h] != 1):
                flag = 0
                break
            l += 1
            h -= 1
    if flag:
        print('yes')
    else:
        print('no')
