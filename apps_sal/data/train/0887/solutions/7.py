
def calculate_min_path(A,B):
 flag = 1
 if A[0] != 0 or B[n-1] != 0:
  print("No")
  return
 
 if A[n-1] != B[0]:
  print("No")
  return
  
 for i in range(1,n-1):
  a = A[i]
  b = A[n-1]
  c = B[i]
  
  if a > 0 and b > 0 and c > 0:
   if a+b < c or a+c < b or b+c < a:
    flag = 0
    break
  else:
   flag = 0
   break
 
  
 if flag == 1:
  print("Yes")
 else:
  print("No")
t=int(input())
for i in range(t):
 n=int(input())
 A = list(map(int, input().split()))
 B = list(map(int, input().split()))
 

 calculate_min_path(A,B)
