t = int(input())
while t > 0:
    s = input()
    (n, c) = s.split(' ')
    n = int(n)
    c = int(c)
    output = 2 + (n - 1) * (2 - 2 / c)
    print(output, end='')
    if t > 1:
        print()
    t -= 1
