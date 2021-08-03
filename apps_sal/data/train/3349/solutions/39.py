def find_missing_number(sequence):

    if sequence == "":

        return 0

    try:

        sequence = set(int(x) for x in sequence.split())

    except ValueError:

        return 1

    for w in range(1, max(sequence) + 1):

        if w not in sequence:

            return w

    return 0
