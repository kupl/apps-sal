def find_missing_number(sequence):
    try:
        nums = list(map(int, sequence.split()))
    except:
        return 1

    max_num = max(nums) if nums else 0
    return (
        min(set(range(1, max_num + 1)) - set(nums))
        if set(range(1, max_num + 1)) != set(nums)
        else 0
    )

