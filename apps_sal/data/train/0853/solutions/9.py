T=int(input())
while T:
 alist=[]
 N=int(input())
 for _ in range(N):
  S=input()
  X=int(input())
  alist.append(tuple([S,X]))
 alist=sorted(alist,key=lambda t1 :t1[1]) 
 for _ in alist:
  print(_[0])
 T-=1 
