# cook your dish here
t=int(input())
for i in  range(t):
    sum1=0
    n=int(input())
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n+1):
        if prime[p]:
            sum1+=p
    print(sum1%10)
    
    

