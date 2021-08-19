from math import sqrt
for t in range(int(input())):
    n = int(input())
    if int(sqrt(n)) == float(sqrt(n)):
        print('YES')
    else:
        print('NO')
