def choose(n, k):
    def factorial(num):
        # a nested function for computing the factorial of the
        # n, k arguments of the choose function
        ra = reversed(list(range(1, num)))
        for r in ra:
            num = num * r
        return num

    # a little of exception handling and conditional reasoning
    # to make deal with edge cases involving negative values
    # and ZeroDivisionError
    try:
        choose = factorial(n) / (factorial(k) * factorial((n - k)))
    except ZeroDivisionError:
        choose = n / k
    if choose < 0:
        return 0
    else:
        return choose
