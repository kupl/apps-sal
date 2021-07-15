def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    arr=[]    
    for p in range(2, n): 
        if prime[p]: 
            arr.append(p)
    if prime[n]:
        arr.append(n)
    return arr        
t=int(input())
for _ in range(t):
    n =int(input())
    k=SieveOfEratosthenes(109)
    count=0
    s=0
    for i in range(2,30):
        if count<n:
            if i in k:
                s+=k[i-1]
                count+=1
            else:
                pass
        else:
            break
    print(s)
            

