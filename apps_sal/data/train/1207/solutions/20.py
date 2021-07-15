# cook your dish here
for i in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 l.sort()
 sum=0
 for j in range(1,len(l)):
  sum+=l[j]
 print(sum*l[0])
