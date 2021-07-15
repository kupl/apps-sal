def dfac ( n ) :
 ans = 1
 for i in range(1,n,2) :
  ans = ans * i
 print(ans)
 
t = eval(input())
for i in range( 1 , t + 1 ) :
 n = eval(input())
 n = n+1 
 dfac ( 2 * n - 1 )

