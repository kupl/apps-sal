# cook your dish here
t = int(input())

for j in range(t):
 m , n = map(int,input().split(" "))
 rx , ry = map(int , input().split(" "))
 steps = int(input())
 route = input()
 
 rak = [0,0]
 
 for i in range(steps):
  #print(route[i])
  if route[i]=='L':
   rak[0] -= 1
  elif route[i]=='R':
   rak[0] += 1
  elif route[i]=='U':
   rak[1] += 1
  elif route[i]=='D':
   rak[1] -= 1
  
  #print(rak[0] , rak[1])
 
 if rak[0]==rx and rak[1]==ry:
  print("Case " + str(j+1)+ ": " +"REACHED")
 
 elif rak[0]>m or rak[0]<0 or rak[1]<0 or rak[1]>n:
  print("Case " + str(j+1)+ ": " +"DANGER")
 
 else:
  print("Case " + str(j+1)+ ": " +"SOMEWHERE")
