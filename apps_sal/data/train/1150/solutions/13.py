x = int(input())
for i in range(x):
    a = int(input())
    j = 0
    while a != 0:
        b = int(a ** 0.5)
        a -= b ** 2
        j += 1
    print(j)
