S = input()
N = int(input())
while N != 0:
    W = input()
    flag = 0
    for i in range(0, len(W)):
        if W[i] in S:
            continue
        else:
            flag = 1
            break
    if flag == 0:
        print('Yes')
    else:
        print('No')
    N -= 1
