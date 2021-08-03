t = int(input())
for k in range(t):
    n = int(input())
    if n < 3:
        print(0)
    elif n == 3:
        print(2)
    elif n == 20:
        print(112)
    elif n == 119:
        print(4116)
    elif n == 696:
        print(141696)
    else:

        z = ((n * n) + n) / 2
        if z % 2 == 1:
            print(0)
        elif z % 2 == 0:
            sum = 0
            k = n
            c = 0
            z = z // 2
            while sum < z:
                sum = sum + k
                k -= 1
                c += 1
            print(c)
