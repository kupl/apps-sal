from itertools import accumulate
def tram(stops, descending, onboarding):
    return max(accumulate(b - a for _, a, b in zip(range(stops), descending, onboarding)))
