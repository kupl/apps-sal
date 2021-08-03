def invite_more_women(arr):
    return abs(sum(filter(lambda x: x < 0, arr))) < sum(filter(lambda x: x > 0, arr))
