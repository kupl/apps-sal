n = int(input())
a = []
b = []
for i in range(1, 1000001):
    s = str(i)
    p = 1
    flag = 0
    for e in s:
        if e == '1':
            flag = 1
        p = p * int(e)
    if p == n:
        if flag != 1:
            a.append(i)
        else:
            b.append(i)
print(len(a), len(b))
