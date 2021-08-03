n = int(input())
x = [int(i) for i in input().split()]
a = 0
b = 0
y1 = []
y2 = []
p = 0
q = 0
for i in range(1, n + 1):
    if x[i - 1] == 1:
        y1.append(i)
        y2.append(i)
    elif x[i - 1] == 2:
        if len(y1) > a:
            a = len(y1)
            p = y1[-1]
        if len(y1) == 1:
            if len(y2) + 1 > b:
                b = len(y2) + 1
                q = y2[0]
            y2 = []
        else:
            y2.append(i)
        y1.pop()
print(a, p, b, q)
