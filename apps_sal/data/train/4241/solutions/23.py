def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    """
    Get the sum of a sequence of integers. Obey the following rules:
     - the sequence is defined by 3 non-negative values: begin, end, step
     - if begin value is greater than the end, function should returns 0
    """
    return sum(range(begin_number, end_number + 1, step))
