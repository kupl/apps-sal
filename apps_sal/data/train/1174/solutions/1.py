from math import *
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(d) for d in input().split()]
    odd,even = 0,0
    for i in range(n):
     if bin(a[i]).count("1")%2 == 1:
      odd += 1
     else:
      even +=1
    total = 0
    if odd >= 3 and even >= 2:
     total += (odd*(odd-1)*(odd-2))//6
     total += odd*(even*(even-1))//2
    elif odd >= 3 and even < 2:
     total +=  (odd*(odd-1)*(odd-2))//6
    elif 0<odd < 3 and even >= 2:
     total +=  odd*(even*(even-1))//2
 
    print(total%(10**9+7))
