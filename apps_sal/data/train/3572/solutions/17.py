def invite_more_women(arr):
    count_women = 0
    count_men = 0
    for element in arr:
        if element == 1:
            count_men += 1
        else:
            count_women += 1
    if count_women < count_men:
        return True
    else:
        return False
