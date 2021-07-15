# cook your dish here
T = int(input())
for t in range(T):
 N = int(input())
 mat = []
 for i in range(N):
  mat.append(list(map(int, input().strip().split())))
 # print(mat)
 safe = True
 for i in range(N-1):
  for j in range(N-1):
   if mat[i][j] == 1:
    if mat[i+1][j] == 1:
     safe = False
     break
    if mat[i][j+1] == 1:
     safe = False
     break
    # if mat[i-1][j] == 1:
    #     safe = False
    #     break
    # if mat[i-1][j] == 1:
    #     safe = False
    #     break
    
  if not safe:
   # print("UNSAFE")
   break
 if safe:
  print("SAFE")
 else:
  print("UNSAFE")
     

