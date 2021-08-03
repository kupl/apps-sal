from collections import *
for _ in range(int(input())):
    str1 = input()
    str2 = input()
    x = Counter(str1)
    y = Counter(str2)
    count = 0
    for i in x:
        count += min(x[i], y[i])
    print(count)
