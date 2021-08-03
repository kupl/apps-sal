def invite_more_women(arr):
    count_woman = arr.count(1)
    count_man = arr.count(-1)

    return True if count_woman - count_man >= 1 else False
