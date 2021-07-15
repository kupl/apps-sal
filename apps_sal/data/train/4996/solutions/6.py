def ffb(n):
    a, b = 1, 1
    for i in range(n):
        if a % 15 == 0:
            yield 'FizzBuzz'
        elif a % 3 == 0:
            yield 'Fizz'
        elif a % 5 == 0:
            yield 'Buzz'
        else:
            yield a
        a, b = b, a + b


def fibs_fizz_buzz(n):
    return list(ffb(n))
