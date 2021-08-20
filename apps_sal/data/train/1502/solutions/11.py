for _ in range(int(input())):
    s = input().strip()
    n = int(input().strip())
    a = list(input().strip().split())
    a = list(set(a))
    flag = 0
    for i in s:
        if i not in a:
            flag = 1
            break
    if flag == 1:
        print('0')
    else:
        print('1')
