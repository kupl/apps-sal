def invite_more_women(arr):
    countW = 0
    countM = 0
    for i in arr:
        if i == -1:
            countW += 1
        else:
            countM += 1
    return countW < countM
