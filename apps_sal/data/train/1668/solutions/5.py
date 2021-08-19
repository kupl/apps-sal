def next_smaller(n):
    nums = list(map(int, list(str(n))))
    seen = []
    for i in reversed(range(1, len(nums))):
        if nums[i - 1] > nums[i]:
            seen.append(nums[i])
            seen.append(nums[i - 1])
            seen = sorted(seen, reverse=True)
            for j in range(len(seen)):
                if seen[j] < nums[i - 1]:
                    winner = seen.pop(j)
                    break
            if winner == 0 and i == 1:
                return -1
            nums = nums[:i - 1]
            nums.append(winner)
            nums.extend(seen)
            return int(''.join(map(str, nums)))
        else:
            seen.append(nums[i])
    return -1
