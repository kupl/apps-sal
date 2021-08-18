def bowling_score(frames):
    rolls = list(frames.replace(' ', ''))
    for i, hit in enumerate(rolls):
        if hit == 'X':
            rolls[i] = 10
        elif hit == '/':
            rolls[i] = 10 - rolls[i - 1]
        else:
            rolls[i] = int(hit)
    score = 0
    for i in range(10):
        frame = rolls.pop(0)
        if frame == 10:
            score += frame + rolls[0] + rolls[1]
        else:
            frame += rolls.pop(0)
            score += frame
            if frame == 10:
                score += rolls[0]
    return score
