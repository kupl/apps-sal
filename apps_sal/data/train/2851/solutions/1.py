import re


def ghostbusters(building):
    bs = re.subn('\s', '', building)
    return bs[0] if bs[1] else "You just wanted my autograph didn't you?"
