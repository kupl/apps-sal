def int_rac(n, guess, e=1):
    loop = 0
    while True:
        loop += 1
        old = guess
        guess = (guess + n / guess) // 2
        if abs(old - guess) < e:
            break
    return loop
