import math
t = int(input())
for _ in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    val = a[0]
    index = 0
    for i in range(0,len(a)):
        if a[i]<val:
            val = a[i]
            index = i
    print(math.ceil((n)/val))

