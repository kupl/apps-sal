t = int(input())
while(t):
    a = [int(x) for x in input().split()]
    tot = 1 << 4
    flag = 0
    for i in range(1, tot):
        sum = 0
        for j in range(4):
            f = 1 << j
            if(f & i):
                sum += a[j]
        if(sum == 0):
            flag = 1
            break
    print('Yes' if sum == 0 else 'No')
    t -= 1
