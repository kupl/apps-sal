def divisors(x):
    f = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if x // i == i:
                f += 1
            else:
                f += 2
    return f


for _ in range(int(input())):
    (a, b) = map(int, input().split())
    print(divisors(abs(a - b)))
