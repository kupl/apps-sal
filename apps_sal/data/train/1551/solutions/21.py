a = int(input())
k = a
while k != 0:
    x = input().split()
    if 'not' in x:
        print('Real Fancy')
    else:
        print('regularly fancy')
    k = k - 1
