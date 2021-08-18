def did_we_win(plays):
    increment = ["pass", "run"]
    decrement = ["sack"]
    gameOver = ["turnover"]
    score = plays[0][0]
    for x in plays:
        if(x):
            if x[1] in increment:
                score += x[0]
            elif x[1] in decrement:
                score -= x[0]
            else:
                return False
    if (score - plays[0][0]) > 10:
        return True
    else:
        return False
