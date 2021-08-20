from itertools import count


def find_missing_number(sequence):
    try:
        seq = sorted(map(int, sequence.split()))
        return next((a for (a, b) in zip(count(1), seq) if a != b))
    except ValueError:
        return 1
    except StopIteration:
        return 0
