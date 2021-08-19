for _ in range(int(input())):
    (a, b, c, d) = list(map(int, input().split()))
    flag = 0
    if a == 0 or b == 0 or c == 0 or (d == 0):
        print('Yes')
        flag = 1
    l = [a, b, c, d]
    if flag == 0:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == 0:
                    print('Yes')
                    flag = 1
                    break
    if flag == 0:
        if a + c + d == 0 or b + c + d == 0 or a + b + c == 0 or (a + b + d == 0):
            flag = 1
            print('Yes')
    if flag == 0:
        if a + b + c + d == 0:
            print('Yes')
            flag = 1
    if flag == 0:
        print('No')
