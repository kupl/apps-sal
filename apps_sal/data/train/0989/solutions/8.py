t = int(input())
for i in range(t):
    (x, y, k) = list(map(int, input().split()))
    a = (x + y) // k
    if a % 2 == 0:
        print('Chef')
    else:
        print('Paja')
