# cook your dish here
g=10**9+7
for _ in range(int(input())):
 l=list(map(int,input().split()))
 l.sort()
 m=l[0]*(l[1]-1)*(l[2]-2)
 print(m%g)

