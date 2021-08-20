def find_missing_number(sequence):
    try:
        nums = set(map(int, sequence.split()))
        try:
            return min((c for c in range(1, max(nums)) if c not in nums))
        except:
            return 0
    except:
        return 1
