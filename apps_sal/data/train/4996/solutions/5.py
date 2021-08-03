def fizz_buzz(n):
    return "FizzBuzz" if not n % 15 else "Buzz" if not n % 5 else "Fizz" if not n % 3 else n


def fibs_generator(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibs_fizz_buzz(n):
    return [fizz_buzz(x) for x in fibs_generator(n)]
