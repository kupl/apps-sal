def points(games):
    score = 0
    for game in games :
        (x, y) = tuple(game.split(':'))
        if x > y :
            score+=3
        elif x==y :
            score+=1
    return score
