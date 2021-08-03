# A spooky string is one with whitespace.  We must de-spook the given string
def ghostbusters(spookyStr):

    charToRemove = ' '  # whitespace
    deSpookedStr = spookyStr.replace(charToRemove, "")

    if deSpookedStr == spookyStr:
        deSpookedStr = "You just wanted my autograph didn't you?"

    return deSpookedStr
# ---end fun
