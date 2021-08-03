# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    num = int(k / n)
    if (k / n == num):
        print(0)
    else:
        x = max(n * (1 + num) - k, 0)
        diff = abs(x - (n - x))
        if diff == 0:
            number = 2 * x - 1
        else:
            number = min(x, n - x) * 2
        print(number)
