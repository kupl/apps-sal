def sum_int(i):
    """Sum digits of an integer - standard"""
    s = 0
    while i != 0:
        s += i % 10
        i //= 10
    return s


def find_4digs(m, MaxNum, MaxSum):
    """start by finding all 4 digit numbers n m \\leq n \\leq MaxNum with sum \\leq MaxSum"""
    sts = [m]
    for i in range(0, 4):
        for st in sts:
            while sum_int(st + 10 ** i) <= MaxSum and st + 10 ** i <= MaxNum:
                sts.append(st + 10 ** i)
                st += 10 ** i
    sts = list(set(sts))
    return sts


def find_5digs(nums, MaxNum, MaxSum):
    """ takes in a list of 4 digit numbers \\leq MaxNum and with sum \\leq MaxSum. Returns list of 4 and 5 digit nums 
    with every consecutive 4 digits satisfying the same conditions"""
    for s in nums:
        for i in range(1, MaxSum - sum_int(int(str(s)[0:3])) + 1):
            cand1 = int(str(i) + str(s))
            if cand1 <= MaxNum:
                nums.append(cand1)
        for i in range(0, MaxSum - sum_int(int(str(s)[1:4])) + 1):
            cand2 = int(str(s) + str(i))
            if cand2 <= MaxNum:
                nums.append(cand2)
    nums = list(set(nums))
    return nums


def max_sumDig(MaxNum, MaxSum):
    """ Find all numbers satisfying the conditions. """
    nums = find_4digs(1000, MaxNum, MaxSum)
    nums = find_5digs(nums, MaxNum, MaxSum)
    mean = sum(nums) / len(nums)
    dists = [abs(s - mean) for s in nums]
    for i in range(len(dists)):
        if dists[i] == min(dists):
            min_dist = nums[i]
    return [len(nums), min_dist, sum(nums)]
