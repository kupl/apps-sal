t=int(input())
for i in range(t):
 a=list(map(int,input().split()))
 n,r=a[0],a[1]
 w=(n*((n-1)**(r)))%((10**9)+7)
 
 print(w)
