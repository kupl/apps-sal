t = int(input())
while(t):
    t = t - 1
    l = list(map(int, input().split()))
    X = l[0]
    K = l[1]
    sum1 = 0
    sum2 = 0
    for i in range(2, X + 1):
        if(X % i == 0):
            sum1 = sum1 + i**K
    for i in range(2, K + 1):
        if(K % i == 0):
            sum2 = sum2 + X * i
    print(str(sum1) + " " + str(sum2))
