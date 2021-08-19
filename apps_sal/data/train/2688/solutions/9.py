def repeat_sequence_len(n):
    (seen, i) = ({}, 0)
    n = sum([int(x) ** 2 for x in str(n)])
    while n not in seen:
        seen[n] = i
        n = sum([int(x) ** 2 for x in str(n)])
        i += 1
    return i - seen[n]
