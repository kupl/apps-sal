# cook your dish here
t=int(input())
for i in range(t):
 n,k=list(map(int,input().split()))
 s=list(map(int,input().split()))

 s.sort()
 su=sum(s)
 s1=sum(s[:k])
 s2=sum(s[n-k:])

 print(max(abs(s1-(su-s1)),abs(s2-(su-s2))))

 

