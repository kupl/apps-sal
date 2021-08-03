length = int(input())
brackets = [int(i) for i in input().split()]
alternateDepths = []
squareSymbols, roundedSymbols = 0, 0

lastAlternatedLevel, lastAlternatedBracket, alDepth, level = [None], [None], 0, 0
lowestSquareHeight, lowestRoundedHeight = float("inf"), float("inf")
betweenSquare, betweenRounded = 0, 0
for i in brackets:
    if lowestRoundedHeight != float("inf"):
        betweenRounded += 1
    if lowestSquareHeight != float("inf"):
        betweenSquare += 1

    if i in [1, 3]:
        level += 1
        if i != lastAlternatedBracket[-1]:
            alDepth += 1
            lastAlternatedBracket.append(i)
            lastAlternatedLevel.append(level)
        if i == 1 and level < lowestRoundedHeight:
            # print("Setting Rounded", level)
            lowestRoundedHeight = level
            betweenRounded += 1
        elif i == 3 and level < lowestSquareHeight:
            lowestSquareHeight = level
            betweenSquare += 1
    else:
        if i == lastAlternatedBracket[-1] + 1 and level == lastAlternatedLevel[-1]:
            alternateDepths.append(alDepth)
            alDepth -= 1
            lastAlternatedLevel.pop()
            lastAlternatedBracket.pop()

        if i == 2 and level == lowestRoundedHeight:
            # print("here1", betweenRounded)
            if betweenRounded > roundedSymbols:
                roundedSymbols = betweenRounded
            lowestRoundedHeight = float("inf")
            betweenRounded = 0

        if i == 4 and level == lowestSquareHeight:
            if betweenSquare > squareSymbols:
                squareSymbols = betweenSquare
            lowestSquareHeight = float("inf")
            betweenSquare = 0

        level -= 1

print(max(alternateDepths), roundedSymbols, squareSymbols)
