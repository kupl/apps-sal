import re


def ant_bridge(ants, terrain):
    nGap = sum(2 + len(gap) - (free == '-') for free, gap in re.findall(r'(-+)(\.+)', '-' + terrain)) % len(ants)
    return ants[-nGap:] + ants[:-nGap]
