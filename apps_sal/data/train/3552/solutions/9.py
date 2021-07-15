def update_score(current_score, called_trump, alone, tricks):
    score=current_score[:]
    c=tricks.count(called_trump)
    i=called_trump-1
    if c<=2:
        score[i^1]+=2
    elif c<5:
        score[i]+=1
    elif alone:
        score[i]+=4
    else:
        score[i]+=2
    return score
