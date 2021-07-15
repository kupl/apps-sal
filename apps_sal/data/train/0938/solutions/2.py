def repeats(A,x):
 for i in range(N):
  if(x==A[i]):
   return i
 return -1

def assign_indices(A,newA):
 for i in range(N):
  x=repeats(A,A[i])
  if(x==-1):
   newA[i]=i
  else:
   newA[i]=x

T=int(input())

for t in range(T):
 N=int(input())
 A=input().split(" ")

 indices=[0 for x in range(1005)]

 for i in range(N):
  A[i]=int(A[i])

 assign_indices(A,indices)
 total=0
 taken=[]

 for i in range(N-1):
  taken=[0 for x in range(1005)]
  for j in range(i,N):
   before=0
   taken[indices[j]]+=1
   for k in range(j+1,N):
    if(taken[indices[k]]==0):
     total=total+(k-j)-before
    else:
     before=k-j

 print(total)

