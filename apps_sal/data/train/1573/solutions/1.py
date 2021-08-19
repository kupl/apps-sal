def calc(n):
    a = n * (n - 1)
    a = int(a / 2)
    return a


t = int(input())
tt = 0
while tt < t:
    tt = tt + 1
    n = int(input())
    num = calc(n)
    if num % n != 0:
        print('NO')
    else:
        win = int(num / n)
        print('YES')
        i = 0
        while i < n:
            i = i + 1
            j = i
            str = ''
            k = 0
            while k < n:
                str = str + '0'
                k = k + 1
            k = 0
            while k < win:
                if (j + k) % n == 0:
                    str = '1' + str[1:n]
                elif (j + k) % n == n - 1:
                    str = str[:n - 1] + '1'
                else:
                    kkk = (j + k) % n
                    str = str[0:kkk] + '1' + str[kkk + 1:]
                k = k + 1
            print(str)
