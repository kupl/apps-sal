def find_outlier(integers):
    evens = []
    odds = []
    for each in integers:
        if each % 2 == 0:
            evens.append(each)
        else:
            odds.append(each)
        if len(evens) > 1 and len(odds) == 1:
            return odds[0]
        elif len(odds) > 1 and len(evens) == 1:
            return evens[0]
