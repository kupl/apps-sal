x = int(input())
for i in range(x):
    c = 0
    y = int(input())
    while y > 0:
        c = c + y * y
        y = y - 2
    print(c)
