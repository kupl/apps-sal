def amidakuji(ar):
    # Set up original number list
    nums = list(range(len(ar[0]) + 1))
    # For each layer:
    for layer in ar:
        # Swap the positions of numbers at each rung
        for pos in range(len(ar[0])):
            if layer[pos] == "1":
                nums[pos], nums[pos + 1] = nums[pos + 1], nums[pos]
    return nums
