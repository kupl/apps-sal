
from math import ceil
from bisect import bisect_right as b_r
from bisect import bisect_left as b_l
ar = list(map(int , input().split()))
a = [int(ceil((ar[1]-int(x)+1)/ar[2])) for x in input().split()]
s = sum(a)
ar[1] = max(a)
m = ar[1] - (s-ar[1])%2
mi = s%2 
print(int( (m-mi)//2 +1)%(10**9+7))


