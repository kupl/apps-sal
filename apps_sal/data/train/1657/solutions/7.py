def string_func(s, x):
    len_s = len(s)
    arr = list(s)
    mapping = []
    correct_seq = list(range(len_s))
    changed_seq = correct_seq[:]
    for i in range(int(len_s / 2 + 0.5)):
        mapping.append(len_s - i - 1)
        mapping.append(i)
    if len_s % 2 != 0:
        mapping.pop()
    for div in range(1, len_s + 1):
        changed_seq = [changed_seq[i] for i in mapping]
        if changed_seq == correct_seq:
            x %= div
            break
    while x:
        arr = [arr[i] for i in mapping]
        x -= 1
    return ''.join(arr)
