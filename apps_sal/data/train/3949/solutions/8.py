from math import ceil
def calculate_tip(a, r):
    d = dict(zip(['terrible', 'poor','good','great','excellent'], [0, 5, 10, 15, 20]))
    r = r.lower()
    if r in d:
        return (ceil(d[r]*a/100))
    else:
        return 'Rating not recognised'
