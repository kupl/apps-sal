# cook your dish here
import math
read = lambda : list(map(int,input().strip.split()))
rs =lambda: int(input().strip())
t = rs()
ans = []
def find(x):
    i = 0
    x = x-1;
    while(x):
        x = x>>1;
        i += 1;
    return 1 <<i

for i in range(t):
    n = rs()
    ans.append(find(n))
print("\n".join([str(x) for x in ans]))
