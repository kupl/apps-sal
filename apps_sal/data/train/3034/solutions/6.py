def bowling_score(rolls):
    (i, score) = (0, 0)
    for _ in range(10):
        oneBall = frame = rolls[i]
        i += 1
        if oneBall < 10:
            frame += rolls[i]
            i += 1
        if frame == 10:
            score += sum(rolls[i:i + 1 + (oneBall == 10)])
        score += frame
    return score
