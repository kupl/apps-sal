def positive_sum(arr):
    """ I really hate these one line codes, but here I am...
        trying to be cool here... and writing some"""
    return sum([x if x > 0 else 0 for x in arr])
