t = int(input())
for _ in range(t):
    (n, x) = (int(x) for x in input().split())
    (s, l) = input().split()
    if s == 'R':
        x = n - x + 1
    if l == 'E':
        if x % 2 == 0:
            l = 'H'
        else:
            l = 'E'
    elif l == 'H':
        if x % 2 == 0:
            l = 'E'
        else:
            l = 'H'
    print(x, l)
