for _ in range(int(input())):
    n = int(input())
    flag = 0
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        for j in range(i + 1, n):
            if 2000 - a[i] == a[j]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        print('Accepted')
    else:
        print('Rejected')
