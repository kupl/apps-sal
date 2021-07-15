import re
for _ in range(int(input())):
    m = re.match("1+(0*)", input())
    if m:
        print(len(m[1]))
    else:
        print(0)

