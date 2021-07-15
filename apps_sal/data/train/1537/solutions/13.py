def s(n):
    res = []
    prime = [True for i in range(n+1)] 
    p = 2
    for i in range(2,int(n ** 0.5)+ 1):
        if prime[i]:
            j = 2
            while i * j <= n:
                prime[i * j] = False
                j += 1
    for p in range(2, n+1): 
        if prime[p]: 
            res.append(p)
    return res
o = s(100000)
for _ in range(int(input())):
    n = int(input())
    sum = 0
    for i in range(n):
        temp = o[i]
        sum += o[temp-1]
    print(sum)
