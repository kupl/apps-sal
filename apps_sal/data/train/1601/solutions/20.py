# cook your dish here
ts=int(input())
while ts>0:
 num,p=list(map(int,input().split()))
 aa=(num//2)+1
 if(num==1 or num==2):
  print(p*p*p)
 else:
  aa=num%aa
  b=(p-aa)**2
  c=(p-num)*(p-aa)
  a=(p-num)*(p-num)
  print(b+c+a)
 ts=ts-1


