for i in range(int(input())):
 n=int(input())
 t=list(map(int,input().split()))[:n]
 m=[]
 for j in range(len(t)):
  for k in range(j+1,len(t)):
   m.append(t[j]+t[k])
 print(m.count(max(m))/((n*(n-1))/2))
