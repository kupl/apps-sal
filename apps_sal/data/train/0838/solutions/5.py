for _ in range(int(input())):
 n=int(input())
 l=[int(x) for x in input().split()]
 l.reverse()
 x=l[0]
 x=x+1 
 for i in range(1,n):
  x=max(x,l[i])
  x=x+1 
 print(x-1)
 

