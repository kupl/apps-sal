def min_value(digits):

    nums = sorted(list(set(digits)))
    s = ''

    for i in nums:

        s += str(i)
    return int(s)
