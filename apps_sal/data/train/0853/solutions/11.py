t=int(input())
for _ in range(t):
 n=int(input())
 arr=[]
 for i in range(n):
  pos=[]
  name=input()
  time=int(input())
  pos.append(time)
  pos.append(name)
  arr.append(pos)
 arr.sort()
 for i in range(n):
  print(arr[i][1])
