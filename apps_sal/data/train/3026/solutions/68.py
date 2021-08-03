def min_value(digits):
    st = ""
    calc = sorted(list(set(digits)))
    for nums in calc:
        st = st + str(nums)
    return int(st)
