n = int(input())
for i in range(n):
    a = int(input())
    if a % 10 == 0:
        print('0')
    else:
        c = 0
        a = a * 2
        if a % 10 == 0:
            c += 1
            print(c)
        else:
            print('-1')
