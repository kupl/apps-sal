t = int(input())
for i in range(t):
    (x, y, k) = map(int, input().split())
    if (x + y) // k % 2 == 0:
        print('Chef')
    else:
        print('Paja')
