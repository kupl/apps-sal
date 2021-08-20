from itertools import groupby
from statistics import mean


def trump_detector(trump_speech):
    return round(mean((len(list(l)) - 1 for (k, l) in groupby(trump_speech.lower()) if k in 'aeiou')), 2)
