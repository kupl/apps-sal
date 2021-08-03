import math
for t in range(int(input())):
    n = int(input())
    temp = math.sqrt(n)
    if (temp == int(temp)):
        print("YES")
    else:
        print("NO")
