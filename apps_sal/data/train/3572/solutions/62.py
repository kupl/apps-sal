def invite_more_women(arr):
    guys = 0
    gals = 0
    for n in arr:
        if n == 1:
            guys += 1
        if n == -1:
            gals += 1
    if gals > guys or gals == guys:
        return False
    else:
        return True
