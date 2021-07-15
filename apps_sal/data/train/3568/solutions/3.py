from collections import Counter


def bumps(road):
    return "Car Dead" if Counter(road)['n'] > 15 else "Woohoo!"

