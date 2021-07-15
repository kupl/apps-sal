# cook your dish here
t = int(input())

for _ in range(t):
 n = int(input())
 l=[]
 waste = input().split(" ")
 for i in range(n):
  l.append(int(waste[i]))
  
 l.sort()
 for i in range(n//4 + 1):
  
  if i==len(l)//4:
   x = i
   y = x + len(l)//4
   z = y + len(l)//4
   
   #print(x,y,z)
   if l[x]==l[x-1]:
    print(-1)
   elif l[y]==l[y-1]:
    print(-1)
   elif l[z]==l[z-1]:
    print(-1)
   else:
    print(str(l[x]) + " " + str(l[y]) + " " + str(l[z]))
