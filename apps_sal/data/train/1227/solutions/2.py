t=int(input())
for j in range(t):
 f,ba,l,r,t,bo=str(input()).split(" ")
 if(l==f and f==bo):
  print("YES")
 elif(l==f and l==t):
  print("YES")
 elif(l==t and t==ba):
  print("YES")
 elif(l==ba and ba==bo):
  print("YES")
 elif(f==t and t==r):
  print("YES")
 elif(t==ba and ba==r):
  print("YES")
 elif(bo==r and r==f):
  print("YES")
 elif(r==ba and ba==bo):
  print("YES")
 else:
  print("NO")
