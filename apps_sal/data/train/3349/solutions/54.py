def find_missing_number(sequence):
    if sequence == "":
        return(0)
    sequence = sequence.split(' ')
    for i in range(len(sequence)):
        if not sequence[i].isdigit():
            return(1)
        else:
            sequence[i] = int(sequence[i])
    for i in range(1, max(sequence)):
        if i not in sequence:
            return(i)
    return(0)
