def fibs_fizz_buzz(n):
    r, a, b = [], 0, 1
    for i in range(n):
        r.append("Fizz" * (not b % 3) + "Buzz" * (not b % 5) or b)
        a, b = b, a + b
    return r
