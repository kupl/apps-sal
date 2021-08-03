def bowling_score(rolls):
    score = 0
    frame = 0
    i = 0
    while frame < 10:
        if rolls[i] == 10:
            score += rolls[i] + rolls[i + 1] + rolls[i + 2]
            frame += 1
            i += 1
        else:
            tmp = rolls[i] + rolls[i + 1]
            score += tmp
            if tmp == 10:
                score += rolls[i + 2]
            frame += 1
            i += 2
    return score
