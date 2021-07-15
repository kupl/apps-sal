# cook your dish here
for _ in range(int(input())):
 n = int (input())
 arr = list(map(int,input().split()))
 arr.sort()
 c = 0
 for i in range(n):
  
  if arr[i]<= c:
   c+=1

  else:
   break
 print(c)
