def catch_sign_change(lst):
    res = 0
    for i in range(len(lst)-1):
        if (lst[i] >= 0 and lst[i+1] < 0) or (lst[i] < 0 and lst[i+1] >= 0):
            res += 1
    return res
