# cook your dish here
d = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
t = int(input())
for i in range(t):
    s, e, l, r = map(str, input().split())
    l, r = int(l), int(r)
    v = (d.index(e) - d.index(s) + 8) % 7
    c = r + 1
    for i in range(l, r + 1):
        if i % 7 == v:
            c = i
            break
    if c > r:
        print('impossible')
    elif c + 7 <= r:
        print('many')
    else:
        print(c)
