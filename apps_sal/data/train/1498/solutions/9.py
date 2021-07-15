from sys import stdin
from functools import reduce

def factors(n):    
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

for _ in range(int(stdin.readline())):
    h, x, y = list(map(int, stdin.readline().split()))
    arr = factors(h-1)
    ans = 1000000001
    cond = False
    for i in range(len(arr)):
        if arr[i]>=x:
            m = arr[i]-x
            if m%y == 0:
                cond = True
                ans = min(ans, m//y + (h-1)//arr[i])
    if cond == True:
        print(ans)
    else:
        print(-1)
            
            

