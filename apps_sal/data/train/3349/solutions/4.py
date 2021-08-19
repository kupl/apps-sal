def find_missing_number(sequence: str) -> int:
    try:
        elements = set(map(int, sequence.split()))
    except ValueError:
        return 1
    return min(set(range(1, len(elements) + 1)) - elements or [0])
