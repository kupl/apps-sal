t = int(input())
for i in range(t):
    (n, m) = list(map(int, input().strip().split()))
    if n % m % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
