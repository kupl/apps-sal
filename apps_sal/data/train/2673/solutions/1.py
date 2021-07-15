def passer_rating(attempts, yards, completions, touchdowns, interceptions):
    a = (completions / attempts - .3) * 5
    b = (yards / attempts - 3) * .25
    c = (touchdowns / attempts) * 20
    d = 2.375 - (interceptions / attempts * 25)
    a, b, c, d = (max(0, min(x, 2.375)) for x in (a, b, c, d))
    return round((a + b + c + d) / 6 * 100, 1)
