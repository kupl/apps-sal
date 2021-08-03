import copy


def ranks(lst):
    sortedVals = copy.deepcopy(lst)  # need deep copy to not mutate original list
    sortedVals.sort(reverse=True)  # descending order

    rankVec = []
    for v in lst:  # for every value in the list, calculate its rank
        indLoc = sortedVals.index(v)  # always finds first occurance so repetition does not matter
        rankOfVal = indLoc + 1  # min rank is 1 not 0
        rankVec.append(rankOfVal)

    return rankVec
# ---end function
