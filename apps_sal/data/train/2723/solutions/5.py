from numpy import average
nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def average_string(s):
    total = [nums.index(c) for c in s.split(' ') if c in nums]
    return nums[int(average(total))] if len(total) == len(s.split(' ')) else 'n/a'
