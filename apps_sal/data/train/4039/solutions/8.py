def fouriest(i):
    highscore = 0
    winner = 5
    for base in range(5, i - 3, 1):
        fours = 0
        n = i
        while n > 0:
            if n % base == 4:
                fours += 1
            n //= base
        if fours > highscore:
            highscore = fours
            winner = base
        elif 4 * base ** highscore > i:
            break
    n = i
    result = ''
    while n > 0:
        result = str(n % winner) + result if n % winner < 10 else 'x' + result
        n //= winner
    return '{} is the fouriest ({}) in base {}'.format(i, result, winner)
