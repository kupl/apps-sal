def find_missing_number(sequence):
    if len(sequence) == 0:
        return 0

    num = sequence.split()
    if not all(n.isdigit() for n in num):
        return 1

    num = [0] + sorted(map(int, num))
    return next((i for i in range(1, len(num)) if num[i] - num[i - 1] != 1), 0)
