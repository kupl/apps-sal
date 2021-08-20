def invite_more_women(arr):
    intWeman = 0
    intMon = 0
    for i in arr:
        if i == 1:
            intMon += 1
        else:
            intWeman += 1
    if intWeman < intMon:
        return True
    else:
        return False
