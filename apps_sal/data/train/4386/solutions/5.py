def is_in_middle(sequence):
    length = len(sequence)
    if length < 3:
        return False
    if length % 2 != 0:
        index = length // 2 - 1
        if sequence[index:index + 3] == 'abc':
            return True
        return False
    elif length % 2 == 0:
        index1 = length // 2 - 2
        index2 = length // 2 - 1
        if sequence[index1:index1 + 3] == 'abc' or sequence[index2:index2 + 3] == 'abc':
            return True
        return False
