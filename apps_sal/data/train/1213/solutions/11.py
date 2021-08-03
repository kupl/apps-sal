# cook your dish here
for i in range(int(input())):
    x1, x2, x3, v1, v2 = list(map(int, input().split()))
    a = abs(x3 - x1)
    b = abs(x3 - x2)
    x = a / v1
    y = b / v2
    if(x > y):
        print('Kefa')
    elif(x < y):
        print('Chef')
    else:
        print('Draw')
