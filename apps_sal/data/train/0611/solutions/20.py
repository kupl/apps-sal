for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))
 status = False
 for i in range(n):
  a = arr[i]
  for j in range(i+1,n):
   b = arr[j]
   if (a != b) and (arr[a-1] == arr[b-1]):
    status = True
    break
  if status == True:
   break
 if status == True:
  print("Truly Happy")
 else:
  print("Poor Chef")
