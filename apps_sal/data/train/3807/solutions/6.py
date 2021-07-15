def smaller(nums):
    i = 0; res = []
    while i < len(nums):
        j = i + 1; nb = 0
        while j < len(nums):
            if nums[i] > nums[j]:
                nb += 1
            j += 1
        res.append(nb)
        i += 1
    return res
