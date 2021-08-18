for h in range(int(input())):
    x, y, k = map(int, input().split())
    c = (x + y) // k
    if c % 2 == 0:
        print('Chef')
    else:
        print('Paja')
