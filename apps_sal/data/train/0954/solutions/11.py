T=int(input())
for i in range(T):
    n=int(input())
    sum=0
    x = (n * (n + 1)  / 2) 
    sum+= int((x * x))
    for i in range(n-1,0,-1):
        sum+=i*i*i
    print(sum)

