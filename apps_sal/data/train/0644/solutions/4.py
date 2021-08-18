test = int(input())
while(test > 0):
    n = int(input())
    l = list(map(int, input().split()))
    cnt = 0
    for x in l:
        if(x > 1):
            cnt += (x - 1)
    if(cnt % n == 0):
        print('Yes')
    else:
        print('No')
    test -= 1
