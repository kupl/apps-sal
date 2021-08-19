def amidakuji(ar):
    nums = list(range(len(ar[0]) + 1))
    for layer in ar:
        for pos in range(len(ar[0])):
            if layer[pos] == '1':
                (nums[pos], nums[pos + 1]) = (nums[pos + 1], nums[pos])
    return nums
