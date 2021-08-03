import math
for _ in range(int(input())):
    x = int(input())
    ans = 2 ** math.ceil(math.log2(x))
    print(ans)
