t = int(input())
for s in range(t):
    k = int(input())
    flag = 0
    while k > 0:
        digi = k % 10
        if digi % 2 == 0:
            flag = 1
            break
        k = k // 10
    if flag == 1:
        print(1)
    else:
        print(0)
