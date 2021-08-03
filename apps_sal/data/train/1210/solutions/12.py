t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    a, b = input().split()
    if(a == 'L'):
        if(m % 2 != 0):
            print(m, b)
        else:
            if(b == 'E'):
                print(m, 'H')
            else:
                print(m, 'E')
    else:
        d = n - m + 1
        if(d % 2 != 0):
            print(d, b)
        else:
            if(b == 'E'):
                print(d, 'H')
            else:
                print(d, 'E')
