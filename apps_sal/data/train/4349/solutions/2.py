def int_rac(n, guess):
    count, x = 1, (guess + n / guess) // 2
    while abs(guess - x) >= 1:
        guess, x, count = x, (x + n / x) // 2, count + 1
    return count
