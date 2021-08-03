t = int(input())
for i in range(t):
    n, p = map(int, input().split(" "))
    if n == 1 or n == 2:
        print(p * p * p)
    else:
        if n % 2 == 0:
            m = n // 2 - 1
            z = (p - m) * (p - m) + (p - n) * (p - m) + (p - n) * (p - n)
        else:
            m = n // 2
            z = (p - m) * (p - m) + (p - n) * (p - m) + (p - n) * (p - n)
        print(z)
