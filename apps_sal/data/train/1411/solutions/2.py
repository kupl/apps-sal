import re
for t in range(int(input())):
    list = re.findall('[0-9]+', input())
    a = max(int(list[2]), int(list[3]))
    b = min(int(list[2]), int(list[3]))
    x = int(list[0])
    r2 = int(b * x / a)
    print(x - r2 - 1)
