# cook your dish here
for i in range(int(input())):
    n, d = input().split()
    n = list(n)
    x = int(d)
    y = n.copy()
    for j in range(len(n) - 1, -1, -1):
        if int(y[j]) <= x:
            x = int(y[j])
        else:
            y.pop(j)
    l = len(y)
    for k in range(len(n) - l):
        y.append(d)
    print(''.join(y))
