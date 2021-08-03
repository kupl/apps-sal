def binary_cleaner(seq):
    return [value for value in seq if value == 0 or value == 1], [index for index, value in enumerate(seq) if value not in (0, 1)]
