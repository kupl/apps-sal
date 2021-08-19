t = int(input())
for i in range(t):
    inp = list(map(int, input().split()))
    n = inp[0]
    p = inp[1]
    if n == 1 or n == 2:
        print(p * p * p)
    elif n % 2 == 0:
        print((p - (n // 2 - 1)) ** 2 + (p - n) * (p - (n // 2 - 1)) + (p - n) ** 2)
    else:
        print((p - (n - 1) // 2) ** 2 + (p - n) * (p - (n - 1) // 2) + (p - n) ** 2)
