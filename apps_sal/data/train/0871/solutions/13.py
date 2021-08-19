# cook your dish here
from collections import defaultdict
from math import factorial
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    l = []
    hash = defaultdict(int)
    for i in range(n):
        k = list(input())
        l.append(k)
    ans = 0
    for i in range(n):
        for j in range(m):
            count = 0
            if l[i][j] == 'R':
                x = i
                y = j

                while y < m:
                    if l[x][y] != '#':
                        hash[(count, x, y)] += 1
                    else:
                        break

                    count += 1
                    y += 1

            elif l[i][j] == 'L':
                x = i
                y = j
                count = 0
                while y >= 0:
                    if l[x][y] != '#':
                        hash[(count, x, y)] += 1
                    else:
                        break

                    count += 1

                    y -= 1
            elif l[i][j] == 'U':
                x = i
                y = j
                count = 0
                while x >= 0:
                    if l[x][y] != '#':
                        hash[(count, x, y)] += 1
                    else:
                        break

                    count += 1
                    x -= 1
            elif l[i][j] == 'D':
                x = i
                y = j
                count = 0
                while x < n:
                    if l[x][y] != '#':
                        hash[(count, x, y)] += 1
                    else:
                        break

                    count += 1
                    x += 1

    for i in hash.keys():

        z = hash[i]
        if z > 1:
            ans += factorial(z) // ((factorial(z - 2)) * factorial(2))

    # print(hash.keys())
    print(ans)
