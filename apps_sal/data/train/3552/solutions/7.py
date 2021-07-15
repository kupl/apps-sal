_OUTCOMES = [2,2,2,2,1,1,2,4]

def update_score(current_score, called_trump, alone, tricks):
    score = [0] + current_score
    winner = 1 + (tricks.count(2) > 2)
    i = 4 * (winner == called_trump) + 2 * (tricks.count(winner) == 5) + alone
    score[winner] += _OUTCOMES[i]
    return score[-2:]
