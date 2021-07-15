t=int(input())
for it in range(t):
 n=int(input())
 p=int(((8*n+1)**0.5-3)/2)
 print(n-((p+1)*(p+2))//2)
