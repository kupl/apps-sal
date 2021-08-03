def bowling_score(rolls):
    score = 0
    for i in range(10):
        frame = rolls.pop(0)
        if frame == 10:
            # This is a strike
            score += frame + rolls[0] + rolls[1]
        else:
            frame += rolls.pop(0)
            score += frame
            if frame == 10:
                # This is a spare
                score += rolls[0]
    return score
