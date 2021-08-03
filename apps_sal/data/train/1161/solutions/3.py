# cook your dish here
for i in range(int(input())):
    x = input()
    c = x.count('s')
    d = x.count('m')
    i = 0
    while i < len(x) - 1:
        if x[i] == 's' and x[i + 1] == 'm' or x[i] == 'm' and x[i + 1] == 's':
            i += 2
            c -= 1
        else:
            i += 1
    if c > d:
        print("snakes")
    elif d > c:
        print("mongooses")
    else:
        print("tie")
