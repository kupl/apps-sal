testcases=int(input())
for i in range(testcases):
    n=int(input())
    sum1=n*n*(n+1)*(n+1)//4 +(n-1)*(n-1)*(n)*n//4
    print(sum1)
