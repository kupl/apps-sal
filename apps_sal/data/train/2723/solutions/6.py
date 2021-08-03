def average_string(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    d = dict(zip(nums, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    try:
        return nums[sum(d[w] for w in s.split()) // len(s.split())]
    except:
        return 'n/a'
