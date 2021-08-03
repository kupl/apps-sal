def halving_sum(n):
    sums = []
    nums = n
    while nums > 0:
        sums.append(nums)
        nums = int(nums / 2)
        if nums <= 0:
            break
    return sum(sums)
