def summary_ranges(nums):
    (ret, s) = ([], float('-inf'))
    for (e, n) in zip([s] + nums, nums + [-s]):
        if n - e > 1:
            ret.append(['{}', '{}->{}'][s < e].format(s, e))
            s = n
    return ret[1:]
