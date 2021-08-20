def bowling_score(rolls):
    frameIndex = 1
    pins = 10
    rollsLeft = 2
    totalScore = 0
    frameScore = 0
    for i in range(len(rolls)):
        if frameIndex <= 10:
            frameScore += rolls[i]
            pins -= rolls[i]
            rollsLeft -= 1
        if pins <= 0:
            if frameIndex <= 10:
                bonus = rollsLeft + 1
                frameScore += sum(rolls[i + 1:i + 1 + bonus])
            frameIndex += 1
            pins = 10
            rollsLeft = 2
            totalScore += frameScore
            frameScore = 0
        elif rollsLeft <= 0:
            frameIndex += 1
            pins = 10
            rollsLeft = 2
            totalScore += frameScore
            frameScore = 0
    return totalScore
