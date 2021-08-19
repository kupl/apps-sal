def int_rac(n, guess):
    cnt = 0
    while True:
        cnt += 1
        next_guess = (guess + n // guess) // 2
        if next_guess == guess:
            return cnt
        guess = next_guess
