t = int(input())
for i in range(t):
    n = input()
    a = n.split(' ')
    if 'not' in a:
        print('Real Fancy')
    else:
        print('regularly fancy')
