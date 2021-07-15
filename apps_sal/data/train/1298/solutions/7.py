T=int(input())
for i in range(0,T):
 N=int(input())
 a=input().split()
 re=0
 for i in range(1,len(a)):
  if int(a[i])>int(a[0]):
   re+=1
 print(re)

