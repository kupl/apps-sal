def invite_more_women(arr):
    if arr == []:
        return False
    else:
        count1 = 0
        count2 = 0
        for eachnumber in arr:
            if eachnumber == 1:
                count1 = count1 + 1
            elif eachnumber == -1:
                count2 = count2 + abs(eachnumber)
        if count2 > count1 or count2 == count1:
            return False
        else:
            return True
