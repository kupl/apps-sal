from itertools import chain

def days_represented(trips):
    return len(set(chain(*(range(b, e+1) for b, e in trips))))
