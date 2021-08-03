t = eval(input())
while t:
    t -= 1
    n, b, m = list(map(int, input().split()))
    minute = 0
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            minute += n * m
        else:
            n = (n - 1) / 2
            minute += (n + 1) * m
        minute += b
        m *= 2
    print(minute - b)
