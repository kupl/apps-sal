import itertools


# Given the lst of length N, we generate a list of all possible combinations with
#  replacements from choose-1 to choose-N
# Then, for each of the combinations found, simply sum the contents and see if the sum
# matches the target sum
# Example [3, 6, 9, 12] with target sum 12. Here we need a total of 4;
# choose (with replacement) 1 from 4, 2 from 4, 3 from 4, 4 from 4
# Choose 1 [(3,), (6,), (9,), (12,)]
# Choose 2 [(3, 3), (3, 6), (3, 9), (3, 12), (6, 6), (6, 9), (6, 12), (9, 9), (9, 12), (12, 12)]
#           [(3, 3, 3), (3, 3, 6), (3, 3, 9), (3, 3, 12), (3, 6, 6), (3, 6, 9), (3, 6, 12), (3, 9, 9),
#            (3, 9, 12), (3, 12, 12), (6, 6, 6), (6, 6, 9), (6, 6, 12), (6, 9, 9), (6, 9, 12),
#            (6, 12, 12), (9, 9, 9), (9, 9, 12), (9, 12, 12), (12, 12, 12)]
# Choose 3 [(3, 3, 3, 3), (3, 3, 3, 6), (3, 3, 3, 9), (3, 3, 3, 12), (3, 3, 6, 6), (3, 3, 6, 9),
#           (3, 3, 6, 12), (3, 3, 9, 9), (3, 3, 9, 12), (3, 3, 12, 12), (3, 6, 6, 6), (3, 6, 6, 9),
#           (3, 6, 6, 12), (3, 6, 9, 9), (3, 6, 9, 12), (3, 6, 12, 12), (3, 9, 9, 9), (3, 9, 9, 12),
#           (3, 9,12, 12), (3, 12, 12, 12), (6, 6, 6, 6), (6, 6, 6, 9), (6, 6, 6, 12), (6, 6, 9, 9),
#           (6, 6, 9, 12), (6, 6, 12, 12), (6, 9, 9, 9), (6, 9, 9, 12), (6, 9, 12, 12), (6, 12, 12, 12),
#           (9, 9, 9, 9), (9, 9, 9, 12), (9, 9, 12, 12), (9, 12, 12, 12), (12, 12, 12, 12)]
# Now for each we see which sum to the target of 12
def find(lst, targetSum):
    lenList = len(lst)

    combWithReplacementList = []
    for chooseR in range(1, lenList + 1):
        combsChooseR = itertools.combinations_with_replacement(lst, chooseR)
        combWithReplacementList.append(list(combsChooseR))

    totalFound = 0
    for col in combWithReplacementList:
        for combChoice in col:
            if (sum(combChoice)) == targetSum:
                totalFound += 1

    return totalFound
# ----end function
