m = int(input())
for i in range(0, m):
    n = int(input())
    a = list(map(int, input().strip().split()))
    l = len(a)
    j = 0
    max = -999999
    while(j < l):
        sum = 0
        if(j == (l - 1)):
            sum = a[j] + a[0] + a[1]
        elif(j == (l - 2)):
            sum = a[j] + a[j + 1] + a[0]
        else:
            sum = a[j] + a[j + 1] + a[j + 2]
        if(sum > max):
            max = sum
        j = j + 1
    print(max)
