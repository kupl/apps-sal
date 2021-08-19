def fibs_fizz_buzz(n):
    (a, b, out) = (0, 1, [])
    for i in range(n):
        s = 'Fizz' * (b % 3 == 0) + 'Buzz' * (b % 5 == 0)
        out.append(s if s else b)
        (a, b) = (b, a + b)
    return out
