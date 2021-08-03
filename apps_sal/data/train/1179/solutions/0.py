# cook your dish here
from math import sqrt
for _ in range(int(input())):
    n = int(input())
    sum = (n * (n + 1)) // 2
    # print(sum)
    if(sum % 2 != 0):
        print(0)
        continue
    m = (int((sqrt(1 + 4 * (sum))) - 1) // 2)
    if(m * (m + 1) // 2 == sum // 2):
        print((((m - 1) * m) // 2) + n - m + ((n - m - 1) * (n - m)) // 2)
    else:
        print(n - m)
