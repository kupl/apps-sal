def find_missing(sequence):
    interval = (sequence[-1] - sequence[0]) / len(sequence)
    for (previous, item) in enumerate(sequence[1:]):
        if item - sequence[previous] != interval:
            return item - interval
