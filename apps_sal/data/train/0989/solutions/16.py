t = int(input())
for i in range(t):
    (x, y, k) = list(map(int, input().split()))
    if x + y < k:
        print('Chef')
    elif (x + y) // k % 2 == 0:
        print('Chef')
    elif (x + y) // k % 2 != 0:
        print('Paja')
