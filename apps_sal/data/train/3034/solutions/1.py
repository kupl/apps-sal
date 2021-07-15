def bowling_score(rolls):
    count = 0
    score = 0
    while count < 10:
        count += 1
        frame = rolls.pop(0)
        if frame < 10:
            frame += rolls.pop(0)
            score += frame
            if frame == 10:
                score += rolls[0]
        else:
            score += frame + rolls[0] + rolls[1]
    return score
