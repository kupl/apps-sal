def dfac ( n ) :
 ans = pow(2,n) + 1
 print(ans)
 
t = eval(input())
for i in range( 1 , t + 1 ) :
 n = eval(input()) 
 dfac ( n - 2 )
