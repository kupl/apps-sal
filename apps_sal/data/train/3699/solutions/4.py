import copy


def ranks(lst):
    sortedVals = copy.deepcopy(lst)
    sortedVals.sort(reverse=True)

    rankVec = []
    for v in lst:
        indLoc = sortedVals.index(v)
        rankOfVal = indLoc + 1
        rankVec.append(rankOfVal)

    return rankVec
