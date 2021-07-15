t =int(input()) #no. of test cases
while t>0:
 t=t-1
 str=input()
 size=len(str)
 pos=str.find('W')
 left=pos
 right=size-pos-1
 arr = [[0 for i in range(right+1)] for j in range(left+1)]
 #arr[i,j] = 1 if with i black cells on left and j on right 1st player can         win, 0 otherwise.
 #Recursion: arr[i][j]= or(arr[x][y])
 arr[0][0]=0
 for i in range(left+1):
  for j in range(right+1):
   if i==j:
    arr[i][j]=0
   else:
    arr[i][j]=1
 if(arr[left][right]==1):
  print("Aleksa")
 else:
  print("Chef")

