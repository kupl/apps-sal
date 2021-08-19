(ax, bx) = (0, 0)
for c in input():
    if c == '1':
        ax += 1
for c in input():
    if c == '1':
        bx += 1
print('YES' if bx <= ax + ax % 2 else 'NO')
