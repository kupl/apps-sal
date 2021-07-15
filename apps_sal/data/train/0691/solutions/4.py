for _ in range(int(input())):
 n = int(input())
 lst = list(map(int,input().split()))
 val = 0
 for i in range(n-1,-1,-1):
  temp = 0
  for j in range(i-1,-1,-1):
   if(lst[j]%lst[i] == 0):
    temp = temp + 1
  if(temp >= val):
   val = temp
  if(val == i ):
   break
 print(val)
