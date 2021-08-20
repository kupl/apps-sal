t = int(input())
for i in range(t):
    (n, m) = [int(x) for x in input().split()]
    (a, b) = input().split()
    if a == 'L':
        d = m
    else:
        d = n - m + 1
    if d % 2 != 0:
        print(d, b)
    elif b == 'E':
        print(d, 'H')
    else:
        print(d, 'E')
