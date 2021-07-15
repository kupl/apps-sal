a=int(input())
b=list(map(int,input().split()))
c=list(set(b))
for i in range(0,a+1):
 if i not in c:
  print(i, end=' ')

