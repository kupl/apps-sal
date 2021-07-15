# vivek hirpara
for _ in range(int(input())):
 n=int(input())
 s1=list(map(int,input().split()))
 l2=[]
 for i in s1:
  l2.append(s1.count(i))
 #print(s1,l2)
 print(n-s1.count(s1[l2.index(max(l2))]))
  

