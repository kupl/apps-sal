T = int(input())
for i in range(T):
    A = input()
    B = input()
    flag = 0
    for i in A:
        if i in B:
            flag = 1
            break
    if flag == 0:
        print('No')
    else:
        print('Yes')
