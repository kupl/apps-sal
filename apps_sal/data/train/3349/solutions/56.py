def find_missing_number(sequence):
    if sequence == '':
        return 0
    if [x for x in sequence.split(' ') if x.isnumeric() == False]:
        return 1
    m = max(int(x) for x in sequence.split(' '))
    for x in range(1, m + 1):
        if str(x) not in sequence.split(' '):
            return x
    return 0
