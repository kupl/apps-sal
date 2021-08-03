def crosstable(players, results):
    playersInputRow = {}
    playersScores = {}
    playersSB = {}
    playersSUM = {}
    longestName = float('-inf')
    for number, player in enumerate(players):
        playersInputRow[player] = number
        if len(player) > longestName:
            longestName = len(player)
        playersScores[player] = 0
        for score in results[number]:
            if score != None:
                playersScores[player] += score

    for number, player in enumerate(players):
        playersSB[player] = 0
        for i, score in enumerate(results[number]):
            if score == 0.5:
                playersSB[player] += 0.5 * playersScores[players[i]]
            if score == 1:
                playersSB[player] += playersScores[players[i]]
    for player in players:
        playersSUM[player] = playersScores[player] * 100 + playersSB[player]

    i = 1
    placments = {}
    while playersSUM:
        placments[i] = []
        maxValue = max(playersSUM.values())
        for player in playersSUM:
            if playersSUM[player] == maxValue:
                placments[i].append(player)
        for player in placments[i]:
            del playersSUM[player]
        i += 1

    placmentLength = len(str(len(placments)))
    playersLength = len(str(len(players)))
    ptsLength = len('{:.1f}'.format(max(playersScores.values())))
    sbLength = len('{:.2f}'.format(max(playersSB.values())))

    string = ""
    spaces = "  "
    i = 1
    for place in placments:
        first = True
        for player in sorted(sorted(placments[place]), key=lambda s: s.split()[1]):
            if first == True:
                string += str(i).rjust(placmentLength) + spaces
                first = False
            else:
                string += "".rjust(placmentLength) + spaces
            string += player.ljust(longestName) + spaces
            for place2 in placments:
                for player2 in sorted(sorted(placments[place2]), key=lambda s: s.split()[1]):
                    result = results[playersInputRow[player]][playersInputRow[player2]]
                    if result == None:
                        string += " ".rjust(playersLength) + " "
                    elif result == 1:
                        string += "1".rjust(playersLength) + " "
                    elif result == 0.5:
                        string += "=".rjust(playersLength) + " "
                    elif result == 0:
                        string += "0".rjust(playersLength) + " "
            string += " "
            string += str("{:.1f}".format(playersScores[player])).rjust(ptsLength) + spaces
            string += str("{:.2f}".format((playersSB[player]))).rjust(sbLength)
            if place == 1:
                lineLength = len(string)
            if i != len(players):
                string += "\n"
            i += 1

    head = "#".rjust(placmentLength) + spaces
    head += "Player".ljust(longestName) + spaces
    for i in range(1, len(players) + 1):
        head += str(i).rjust(playersLength) + " "
    head += " "
    head += "Pts".center(ptsLength) + spaces
    head += "SB".center(sbLength - 1)
    while head[-1] == " ":
        head = head[:-1]
    head += "\n"
    head += "".ljust(lineLength, "=") + "\n"

    head += string

    return head

    """
    
    return (
        "#  Player             1 2 3  Pts  SB\n"
        "=====================================\n"
        "1  Boris Spassky        1 =  1.5 1.25\n"
        "2  Garry Kasparov     0   1  1.0 0.50\n"
        "3  Viswanathan Anand  = 0    0.5 0.75")
     """
