def bowling_score(rolls):
    i = score = 0
    for _ in range(10):
        if rolls[i] == 10:
            score += rolls[i] + rolls[i + 1] + rolls[i + 2]
            i += 1
        elif rolls[i] + rolls[i + 1] == 10:
            score += rolls[i] + rolls[i + 1] + rolls[i + 2]
            i += 2
        else:
            score += rolls[i] + rolls[i + 1]
            i += 2
    return score
