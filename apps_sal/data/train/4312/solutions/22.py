def pick_peaks(nums):
    pp_dict = {'pos': [], 'peaks': []}
    size = len(nums)
    i = 1
    for i in range(1, size - 1):
        if nums[i] > nums[i - 1]:
            plateau_start = i
            try:
                while nums[i] == nums[i + 1]:
                    i += 1
                if nums[i] > nums[i + 1]:
                    pp_dict['pos'].append(plateau_start)
                    pp_dict['peaks'].append(nums[plateau_start])
            except LookupError:
                break
    return pp_dict
