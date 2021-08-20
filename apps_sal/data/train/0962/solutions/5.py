t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2:
        m = 1
    else:
        m = 0
    for i in range(n):
        if (i + m) % 2:
            for j in range(n - i):
                print(j + 1, end='')
            print()
        else:
            x = n - i
            while x > 0:
                print(x, end='')
                x -= 1
            print()
