def bowling_score(rolls):
    frames, scores = 0, 0
    while frames < 9:
        scores += sum(rolls[:2])
        if 10 in (rolls[0], sum(rolls[:2])):
            scores += rolls[2]
        if rolls[0] != 10:
            rolls.pop(0)
        frames += 1
        rolls.pop(0)
    return scores + sum(rolls)
