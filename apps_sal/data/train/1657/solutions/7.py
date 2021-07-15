def string_func(s, x):
    len_s = len(s)
    arr = list(s)
    mapping = []
    correct_seq = list(range(len_s))
    changed_seq = correct_seq[:]

    # Make index mapping
    for i in range(int(len_s / 2 + 0.5)):  # the result of placing the indexes
        mapping.append(len_s - i - 1)      # of the once applied "reversal function"
        mapping.append(i)
    if len_s % 2 != 0:
        mapping.pop()

    # Reduce x
    for div in range(1, len_s + 1):                      # take a remainder of the division
        changed_seq = [changed_seq[i] for i in mapping]  # by the distance between repetitions
        if changed_seq == correct_seq:
            x %= div
            break

    while x:
        arr = [arr[i] for i in mapping]
        x -= 1

    return ''.join(arr)
