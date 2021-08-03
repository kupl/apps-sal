x = eval(input())
for i in range(x):
    y = eval(input())
    z = input()
    z = z.split(' ')
    a = int(z[0])
    b = int(z[1])
    while(y > 0):
        temp = min(a, b)
        if a < b:
            b = b - temp
        else:
            a = a - temp
        y = y - 1
    if a > 0 and b > 0:
        chick = a * b
        print("Yes " + str(chick))
    else:
        print("No")
