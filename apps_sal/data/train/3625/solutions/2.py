def sum_of_regular_numbers(arr):
    # (step size, step count, sequence base)
    grouped = [(b - a, 1, a) for a, b in zip(arr[:-1], arr[1:])]
    # Collate the groups by step size
    i = 0
    while i < len(grouped) - 1:
        if grouped[i][0] == grouped[i + 1][0]:
            grouped[i] = (grouped[i][0], grouped[i][1] + 1, grouped[i][2])
            del grouped[i + 1]
        else:
            i += 1
    # Use (first + last) * elements / 2 to find sum of each sequence longer than 2 elements long
    return sum((2 * base + step * steps) * ((steps + 1) / 2) for step, steps, base in grouped if steps >= 2)

