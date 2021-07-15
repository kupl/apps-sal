n=int(input())
while n:
 a,b,c=list(map(int,input().split()))
 m=c//a
 m=(m*a)+b
 if m>c:
 	m-=a
 print(m)
 n-=1

