def catch_sign_change(lst):
    count = 0
    countNumber = 0
    i = 0
    for n in lst:
        if countNumber >= 0 and n < 0 and (i != 0):
            count = count + 1
        elif countNumber < 0 and n >= 0 and (i != 0):
            count = count + 1
        countNumber = n
        i = i + 1
    return count
