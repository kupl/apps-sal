def min_value(digits):
    # your code here

    nums = sorted(list(set(digits)))
    s = ''

    for i in nums:

        s += str(i)
    return int(s)
