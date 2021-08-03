t = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
l = []
for i in range(t):
    n = int(input())
    a = n // 25
    b = n % 25
    if(n % 25 == 0):
        p = s[::-1] * (a)
    else:
        p = s[:1 + b][::-1] + s[::-1] * (a)
    l.append(p)
for i in l:
    print(i)
