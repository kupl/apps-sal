message = "You just wanted my autograph didn't you?"


def ghostbusters(building):
    return building.replace(' ', '') if ' ' in building else message
