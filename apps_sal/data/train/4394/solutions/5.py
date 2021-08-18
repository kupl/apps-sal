def men_still_standing(cards):
    print(cards)
    playersA = {}
    playersB = {}

    countA = 11
    countB = 11

    for i in range(1, 12):
        playersA[i] = 2
        playersB[i] = 2

    for foul in cards:
        team = foul[0]

        countA = 11
        countB = 11

        if len(foul) == 4:
            number = int(foul[1:3])
            cardColor = foul[3]

        else:
            number = int(foul[1])
            cardColor = foul[2]

        if cardColor == 'R':
            cardValue = 2
        else:
            cardValue = 1

        if team == 'A':
            playersA[number] -= cardValue
        else:
            playersB[number] -= cardValue

        for value in list(playersA.values()):
            if value <= 0:
                countA -= 1

        for value in list(playersB.values()):
            if value <= 0:
                countB -= 1

        if countA < 7 or countB < 7:
            return (countA, countB)

    return (countA, countB)
