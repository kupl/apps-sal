n,a,m=eval(input()),list(map(int,input().split())),eval(input())
for i__i in range(m):
 l,r= list(map(int,input().split()))
 l-=1
 Rev,_=a[l:r],0
 Rev.sort()
 d=len(Rev)
 for i_i in range(0,d-1):
  _+=(Rev[i_i+1]-Rev[i_i])*(Rev[i_i+1]-Rev[i_i])
 print(_)

