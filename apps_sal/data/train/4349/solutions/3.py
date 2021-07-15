def int_rac(n, guess):
    t = 0
    while True:
        new = (guess + n//guess)//2
        t += 1
        if new == guess:
            break
        guess = new
    return t
