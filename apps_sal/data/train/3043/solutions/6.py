def print_nums(*nums):
    l = len(str(max(nums, default=0)))
    return "\n".join(f"{n:0{l}d}" for n in nums)
