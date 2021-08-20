import math
inp = input().split(' ')
m = int(inp[0])
n = int(inp[1])
result = []
for column in range(1, math.ceil(m / 2) + 1):
    rowRange = list(range(1, n + 1))
    if column == math.ceil(m / 2) and m % 2 == 1:
        rowRange = list(range(1, math.ceil(n / 2) + 1))
    for row in rowRange:
        result.append(str(column) + ' ' + str(row))
        if row == math.ceil(n / 2) and n % 2 == 1 and (column == math.ceil(m / 2)) and (m % 2 == 1):
            continue
        result.append(str(m + 1 - column) + ' ' + str(n + 1 - row))
print('\n'.join(result))
