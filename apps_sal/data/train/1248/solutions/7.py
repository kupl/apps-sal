for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, n + 1):
        temp = n
        while temp:
            r = temp % i
            temp = temp // i
        if r == 1:
            cnt += 1
    if n == 1:
        print('INFINITY')
    else:
        print(cnt)
