x = int(input())
for i in range(x):
    y = int(input())
    c = 0
    p = 11

    while(y > 0):
        if(y >= pow(2, p)):
            y = y - pow(2, p)
            c = c + 1
        else:
            p = p - 1
    print(c)
