def invite_more_women(arr):
    countMen = 0
    countWomen = 0
    for i in arr:
        if i == 1:
            countMen = countMen + 1
        elif i == -1:
            countWomen = countWomen + 1

    if countWomen < countMen:
        return True
    elif countWomen >= countMen:
        return False
