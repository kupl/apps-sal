for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('0')
    else:
        s = ''
        s2 = ''
        for i in range(n):
            if i % 2 == 0:
                s += '0'
                s2 += '1'
            else:
                s += '1'
                s2 += '0'
        for i in range(n):
            if i % 2 == 0:
                print(s)
            else:
                print(s2)
