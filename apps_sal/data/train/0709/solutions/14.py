# cook your dish here
import math
T = int(input())

for _ in range(T):
    N = int(input())
    ar = input().split()
    m = int(ar[0])
    
    if int(ar[N-1]) > m:
        m = int(ar[N-1])
        
    print(m)
