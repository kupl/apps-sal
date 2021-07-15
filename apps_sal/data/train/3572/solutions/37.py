def invite_more_women(arr):
    count_women = 0
    count_men = 0
    for x in arr:
        if x == -1:
            count_women += 1
        elif x == 1:
            count_men += 1
    #print(count_women)
    #print(count_men)
    if count_men > count_women:
        return True
    else:
        return False
