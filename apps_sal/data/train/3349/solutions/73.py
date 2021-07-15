def find_missing_number(sequence):
    try:
        if not sequence:
            return 0
        elements = list(map(int, sequence.split(' ')))
        start = 1
        for element in sorted(elements):
            if element != start:
                return start
            start += 1
        return 0
    except:
        return 1
