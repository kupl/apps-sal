from itertools import accumulate


def tram(stops, descending, onboarding):
    return max(accumulate(o - d for d, o in zip(descending[:stops], onboarding)))
