def is_in_middle(seq):
    m = len(seq) // 2
    if len(seq) % 2 != 0 and seq[m - 1:m + 2] == 'abc':
        return True
    elif len(seq) % 2 == 0:
        if seq[m - 2:m + 1] == 'abc' or seq[m - 1:m + 2] == 'abc':
            return True
    return False
