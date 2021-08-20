t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    flag = 0
    lst.sort()
    for j in range(len(lst)):
        for k in range(j + 1, len(lst)):
            if lst[j] + lst[k] == 2000:
                print('Accepted')
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        print('Rejected')
