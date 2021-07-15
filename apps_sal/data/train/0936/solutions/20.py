# cook your dish here
def transpose(lst, l):
 for i in range(l):
  for j in range(i,l):
   temp = lst[i][j]
   lst[i][j] = lst[j][i]
   lst[j][i] = temp

def printMatrix(lst):
 for i in lst:
  print(i)

# try:
t = int(input())
while t>0:
 n = int(input())
 lst = []
 bin = list()
 count = 0
 for i in range(n):
  lst.append(list(map(int, input().strip().split())))
 for j in reversed(range(1,n)):
  if not lst[0][j]==j+1:
   count += 1
   transpose(lst, j+1)
 if t==1:
  print(count, end=" ")
 else:
  print(count)

 t = t -1
# except:
#     pass





