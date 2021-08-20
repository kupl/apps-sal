t = int(input())
while t > 0:
    (a, b, c) = map(int, input().split())
    n = (a + b) // c
    if n % 2 == 0:
        print('Chef')
    else:
        print('Paja')
    t -= 1
