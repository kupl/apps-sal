from re import match, sub


def ghostbusters(building):
    return sub('\\s', '', building) if match('.*\\s.*', building) else "You just wanted my autograph didn't you?"
