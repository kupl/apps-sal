from math import ceil


def collatz_steps(min_number, steps):
    (start, interval) = start_and_interval(steps)
    n_intervals = ceil((min_number - start) / interval)
    return start + n_intervals * interval


def start_and_interval(steps):
    """
    The numbers of the kind N = start + k * interval_start are the numbers N which generate the
    sequence :steps: when used as start for the collatz sequence.    
    The numbers of the kind N = end + K * interval_end are the numbers N which result of applying
    the collatz sequence after some steps of :steps:.
    """
    start = 1
    interval_start = 1
    end = 1
    interval_end = 1
    for step in steps:
        if end % 2 == 0:
            expected_next = 'D'
        else:
            expected_next = 'U'
        if step != expected_next:
            start += interval_start
            end += interval_end
        if step == 'D':
            end //= 2
        else:
            end = (end * 3 + 1) // 2
            interval_end *= 3
        interval_start *= 2
    return (start, interval_start)
