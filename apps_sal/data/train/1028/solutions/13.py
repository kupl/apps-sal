N = int(input())
for i in range(N):
    i = int(input())
    x = i % 10
    add = 0
    z = 0
    temp = i
    while temp != 0:
        temp //= 10
        z += 1
    temp = i
    for j in range(z):
        temp = temp // 10
        add += x ** z
        x = temp % 10
    if add == i:
        print('FEELS GOOD')
    else:
        print('FEELS BAD')
