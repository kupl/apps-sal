def choose(n, k):
    def factorial(num):
        ra = reversed(list(range(1, num)))
        for r in ra:
            num = num * r
        return num

    try:
        choose = factorial(n) / (factorial(k) * factorial((n - k)))
    except ZeroDivisionError:
        choose = n / k
    if choose < 0:
        return 0
    else:
        return choose
