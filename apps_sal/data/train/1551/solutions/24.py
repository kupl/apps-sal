t = int(input())
while t:
    s = input()
    l = s.split()
    found = 0
    for x in l:
        if x == 'not':
            found = 1
    if found:
        print('Real Fancy')
    else:
        print('regularly fancy')
    t -= 1
