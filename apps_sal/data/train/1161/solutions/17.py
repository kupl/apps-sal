t = int(input())
for i in range(t):
    a = list(input())
    for i in range(len(a)):
        if a[i] == 'm' and i > 0 and a[i - 1] == 's':
            a[i - 1] = '*'
        elif a[i] == 'm' and i < len(a) - 1 and a[i + 1] == 's':
            a[i + 1] = '*'
    d = a.count('s')
    c = a.count('m')
    if c > d:
        print("mongooses")
    elif d > c:
        print("snakes")
    else:
        print("tie")
