def invite_more_women(arr):
    count_men = 0
    for k in arr:
        if k == 1:
            count_men += 1
    if count_men > len(arr)//2:
        return True
    else:
        return False
