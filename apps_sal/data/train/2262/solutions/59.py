import cmath


r, c, n = map(int, input().split())
lis = []


for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if (0 < x1 < r and 0 < y1 < c) or (0 < x2 < r and 0 < y2 < c):
        continue
    else:
        lis.append((i, x1 - r / 2 + (y1 - c / 2) * 1j))
        lis.append((i, x2 - r / 2 + (y2 - c / 2) * 1j))


lis.sort(key=lambda x: cmath.phase(x[1]))
stack = []


for i in lis:
    if stack == [] or stack[-1] != i[0]:
        stack.append(i[0])
    else:
        stack.pop()

        
if stack == []:
    print("YES")
else:
    print("NO")
