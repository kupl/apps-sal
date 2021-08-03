def find_missing_number(s):
    try:
        nums = set(map(int, s.split()))
    except:
        return 1

    missing = [n for n in range(1, max(nums, default=0) + 1) if n not in nums]

    return min(missing, default=0)
