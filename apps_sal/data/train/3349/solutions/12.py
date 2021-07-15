def find_missing_number(sequence):
    try:
        numbers = list(map(int, sequence.split()))
    except ValueError:
        return 1
    if not numbers: return 0
    all_nums = list(range(1, max(numbers)))
    r = sorted(set(all_nums) - set(numbers))
    return r[0] if len(r) > 0 else 0

