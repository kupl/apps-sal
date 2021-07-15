# cook your dish here
t=int(input())
for _ in range(t):

    [n,k]=[int(x) for x in input().split()]
    if n==0:
        print(((k-1)*k)%1000000007)
        continue
    
    if k%2==0:
        x=int(k/2)-1
        print( ((n+x)*(n+x+1)+ n ) % 1000000007 )
    else:
        x=int((k-3)/2)
        print( ((n+x) * (n+x+1) + n+2*x+2 ) % 1000000007   )
