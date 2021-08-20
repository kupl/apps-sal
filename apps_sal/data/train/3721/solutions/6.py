def catch_sign_change(lst):
    count = 0
    for i in range(len(lst)):
        if i > 0 and 0 <= lst[i] and (lst[i - 1] < 0):
            count += 1
        if i > 0 and lst[i] < 0 and (0 <= lst[i - 1]):
            count += 1
    return count
