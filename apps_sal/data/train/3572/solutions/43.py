def invite_more_women(arr):
    return len([x for x in arr if x == 1]) > len([x for x in arr if x == -1])
