def solution(nums):
    badList = nums
    if badList == None:
        a = []
        return a
    if len(badList) < 2:
        return badList
    else:
        length = len(badList) - 1
        unsorted = True
        while unsorted:
            for element in range(0, length):
                unsorted = False
                if badList[element] > badList[element + 1]:
                    hold = badList[element + 1]
                    badList[element + 1] = badList[element]
                    badList[element] = hold
                else:
                    unsorted = True
        return badList
