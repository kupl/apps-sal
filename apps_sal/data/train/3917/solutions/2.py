def freeway_game(dToExit, myS, cars):
    return sum((cS != myS and (0 < minutes / 60 * cS / (cS - myS) < dToExit / myS) * (-1) ** (cS > myS) for (minutes, cS) in cars))
