def points(games):
    score = 0
    for x in games:
        if x[0] > x[2]:
            score += 3
        if x[0] == x[2]:
            score += 1
    print(score)            
    return score    

