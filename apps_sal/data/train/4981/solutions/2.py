from operator import itemgetter
from numpy import average

def predict(candidates, polls):
    votes = zip(*map(itemgetter(0), polls))
    weights = list(map(itemgetter(1), polls))
    return {x:round1(average(next(votes), weights=weights)) for x in candidates}
