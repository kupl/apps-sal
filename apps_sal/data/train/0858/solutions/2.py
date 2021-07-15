from math import  log2,floor
for _ in range(int(input())):
    n=int(input())

    ans=floor(log2(n))
    print(2**ans)

