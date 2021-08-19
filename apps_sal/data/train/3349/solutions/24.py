def find_missing_number(sequence):
    if not sequence:
        return 0
    sequenceList = list(sequence.split(' '))
    try:
        sequenceInt = [int(i) for i in sequenceList]
    except:
        return 1
    sequenceInt.sort()
    for (i, number) in enumerate(sequenceInt):
        if i + 1 != number:
            return i + 1
    return 0
