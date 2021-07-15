import math
def CountSquares(a, b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
for _ in range(int(input())):
    n=int(input())
    val=CountSquares(1,n)
    ans=val-val//3
    print(ans)
