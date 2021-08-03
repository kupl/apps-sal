def get_last_digit(number: int) -> int:
    """ Get last digit from fibonacci number. """
    fib_seqence = [0, 1]
    for _ in range(1, number):
        fib_seqence.append(fib_seqence[-2] + fib_seqence[-1])
    return int(str(fib_seqence[-1])[-1])
