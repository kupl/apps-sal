# cook your dish here
for t in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 a,b=0,0
 for i in range(n):
  if l[i]>2:
   a+=1
  elif l[i]==2:
   b+=1
 print(int(((a*(a-1)/2)+a*b)))
