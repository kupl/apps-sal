a=int(input())
b=list(map(int,input().split()))

for i in range(0,a+1):
 if i not in b:
  print(i, end=' ')

