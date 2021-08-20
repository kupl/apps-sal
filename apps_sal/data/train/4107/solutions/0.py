from dateutil.parser import parse


def half_life(*persons):
    (p1, p2) = sorted(map(parse, persons))
    return str(p2 + (p2 - p1))[:10]
