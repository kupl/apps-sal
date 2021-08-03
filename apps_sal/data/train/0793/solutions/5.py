# cook your dish here
import math
n, r = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a = sorted(a + [r])
diff = []
# print(a)
for i in range(0, len(a) - 1):
    diff.append(abs(a[i + 1] - a[i]))
# print(diff)
if len(diff) == 1:
    print(diff[0])
else:
    flag = 0
    g = math.gcd(diff[0], diff[1])
    for i in range(2, len(diff)):
        if g == 1:
            print(g)
            flag = 1
            break
        g = math.gcd(diff[i], g)
    if flag == 0:
        print(g)
