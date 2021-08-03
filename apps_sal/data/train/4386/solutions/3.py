def is_in_middle(sequence):
    n = len(sequence)
    i = (n - 3) // 2
    return sequence[i:i + 3] == 'abc' or (n % 2 == 0 and sequence[i + 1:i + 4] == 'abc')
