arr = {}
temp = input().split(" ")
n = int(temp[0])
m = int(temp[1])
for i in range(n):
 temp1 = input().split(" ")
 for j in range(m):
  arr[i ,j] = int(temp1[j])

t = eval(input())
for k in range(int(t)):
 temp2 = input().split(" ")
 x1 = int(temp2[0])
 y1 = int(temp2[1])
 x2 = int(temp2[2])
 y2 = int(temp2[3])
 total = 0
 for l in range(x1,x2+1):
  for m in range(y1,y2+1):
   total = total + arr[l-1,m-1]
 print(total)

