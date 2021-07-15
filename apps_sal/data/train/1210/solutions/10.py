# cook your dish here
T=int(input())
for i in range(T):
 N=input().split() 
 for i in range(len(N)):
  N[i]=int(N[i]) 
 X=input().split() 
 
 if(X[0]=='L' and X[1]=='H'):
  if(N[1]%2==0):
   print(str(N[1])+" E")
  else:
   print(str(N[1])+" H") 
   
 if(X[0]=='L' and X[1]=='E'):
  if(N[1]%2==0):
   print(str(N[1])+" H")
  else:
   print(str(N[1])+" E")
   
   
   
 if(X[0]=='R' and X[1]=='E' and N[0]%2==0):
  if(N[1]%2==0):
   print(str((N[0]-N[1])+1)+" E")
  else:
   print(str((N[0]-N[1])+1)+" H")
   
 if(X[0]=='R' and X[1]=='E' and N[0]%2!=0):
  if(N[1]%2==0):
   print(str((N[0]-N[1])+1)+" H")
  else:
   print(str((N[0]-N[1])+1)+" E") 
   
   
   
 if(X[0]=='R' and X[1]=='H' and N[0]%2==0):
  if(N[1]%2==0):
   print(str((N[0]-N[1])+1)+" H")
  else:
   print(str((N[0]-N[1])+1)+" E")
   
 if(X[0]=='R' and X[1]=='H' and N[0]%2!=0):
  if(N[1]%2==0):
   print(str((N[0]-N[1])+1)+" E")
  else:
   print(str((N[0]-N[1])+1)+" H")
