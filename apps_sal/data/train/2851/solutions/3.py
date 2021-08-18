def ghostbusters(spookyStr):

    charToRemove = ' '
    deSpookedStr = spookyStr.replace(charToRemove, "")

    if deSpookedStr == spookyStr:
        deSpookedStr = "You just wanted my autograph didn't you?"

    return deSpookedStr
