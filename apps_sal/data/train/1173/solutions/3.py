# cook your dish here
from functools import reduce
from operator import xor 

for _ in range(int(input())):
 n = int( input() )
 a = list( map( int, input().split() ) )
 
 ans = 0
 
 for i in range(1, n):
  for j in range(i):
   res = reduce(xor, a[j:j+n-i+1])
   #print(res, a[j:j+n-i+1])
   if( res == 0 ):
    ans += n-i
    
 print(ans)
