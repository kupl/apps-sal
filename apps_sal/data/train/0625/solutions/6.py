def solve(n, l):
    k = 10
    d =[] 
    for i in range(k + 1): 
        d.append(0) 
    cumSum = 0
    for i in range(n): 
        cumSum = cumSum + l[i] 
        d[((cumSum % k)+k)% k]= d[((cumSum % k)+k)% k] + 1
    result = 0 
    for i in range(k):  
        if (d[i] > 1): 
            result = result + (d[i]*(d[i]-1))//2
    result = result + d[0] 
       
    return result  

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n):
        l[i]=int(l[i]/100000000)
    print(solve(n, l)) 
