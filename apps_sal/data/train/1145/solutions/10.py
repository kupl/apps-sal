t = eval(input())
for i in range(t):
    n = eval(input())
    if n % 2 == 0:
        print('0')
    else:
        s = ''
        while n > 3:
            if (n + 1) / 2 % 2 == 1:
                s += '1'
                n = (n + 1) / 2
            else:
                s += '2'
                n = (n - 1) / 2
        print('2' + s[::-1])
