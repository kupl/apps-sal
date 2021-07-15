import math
t=int(input())
for i in range(t):
    n=int(input())
    alpha=list(map(int,input().split()))
    beta=math.factorial(n-1)
    sumfinal=int('1'*n)*sum(alpha)*beta
    print(sumfinal)
    
    

