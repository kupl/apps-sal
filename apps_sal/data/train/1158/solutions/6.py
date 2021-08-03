n = int(input())
res = 0
while n > 0:
    n -= 1
    s = input()
    l = s.split()
    x = l[-1]
    e = 0
    f = 0
    t = 0
    for ch in x:
        if ch == '8':
            e += 1
        elif ch == '5':
            f += 1
        elif ch == '3':
            t += 1
        else:
            t = 1001
            break
    if(e >= f >= t):
        res += 1
print(res)
