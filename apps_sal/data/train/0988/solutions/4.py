import operator
t=int(input())
for z in range(t):
  n=int(input())
  lis=list(map(int,input().split()))
  lis2=[0]*32
  for i in range(n):
    a=bin(lis[i])[2:]
    for i in range(len(a)):
      if a[i]=='1':
        lis2[len(a)-i-1]+=1
  ss=''
  lis2.reverse()
  #print(lis2)
  for i in lis2:
    if i>n//2:
      ss+='1'
    else:
      ss+='0'
  #print(ss)
  aa=int(ss,2)
  s=0
  for i in lis:
    s+=i^aa
  print(s)

