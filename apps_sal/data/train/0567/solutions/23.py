

t = int(input())

for i in range(t):
    n = int(input())
    flag = 0
    l = list(map(int, input().split()))
    for j in range(n - 2):
        if l[j] == l[j + 1] == l[j + 2]:
            flag = 1
            break
    if flag == 1:
        print('Yes')
    else:
        print('No')
