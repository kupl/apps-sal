def f(n):
    if type(n) == int and n > 0:
        a = 0
        sum = 0
        while a < n:
            a = a + 1
            sum = sum + a
        return sum
