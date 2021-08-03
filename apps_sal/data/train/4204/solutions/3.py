def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    n = 1
    num = max(num, 11)
    minus, plus = num, num
    def f(x): return str(x) == str(x)[::-1]
    pal = 0 if not f(num) else num
    while not pal:
        plus += n
        if f(plus):
            return plus
        minus -= n
        if f(minus):
            return minus
    return pal
