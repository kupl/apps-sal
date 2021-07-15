for i in range(int(input())):
    n,k = map(int,input().split())
    arr = list()
    var1 = 0
    for j in range(2,n+1):
        if n%j==0:
            arr.append(j)
            var1 = var1 + j**k
    var2 = 0
    for j in range(2,k+1):
        if k%j==0:
            var2 = var2 + n*j
    print(var1,var2)
