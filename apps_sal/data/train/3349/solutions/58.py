def find_missing_number(sequence):
    try:
        sequence = [int(num) for num in sequence.split()]
        nums = set(sequence)
        for i in range(1, len(sequence) + 1):
            if i not in nums:
                return i
        return 0
    except ValueError:
        return 1
