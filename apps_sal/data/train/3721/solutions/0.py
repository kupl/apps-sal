def catch_sign_change(lst):
    count = 0
    for i in range(1,len(lst)):
        if lst[i] < 0 and lst[i-1] >= 0:count += 1
        if lst[i] >= 0 and lst[i-1] < 0:count += 1
    return count
