import re
def solve(s):
    nums = re.findall('\d+', s )
    nums = [int(i) for i in nums]
    return max(nums)
