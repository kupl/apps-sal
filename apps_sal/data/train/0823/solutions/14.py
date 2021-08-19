t = int(input())
for _ in range(t):
    l = list(map(int, input().split(' ')))
    flag = False
    tot = 1 << len(l)
    for i in range(tot):
        sum = 0
        c = 0
        for j in range(len(l)):
            k = 1 << j
            if i & k != 0:
                sum = sum + l[j]
                c = c + 1
        if sum == 0 and c != 0:
            print('Yes')
            flag = True
            break
    if flag == False:
        print('No')
