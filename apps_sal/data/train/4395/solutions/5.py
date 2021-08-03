from collections import Counter


def next_higher(prev: int) -> int:
    """
    Consider the integer as a binary integer, left-padded with a zero. To find
    the next binary integer with the same number of bits we must swap (to
    preserve the number of set bits) the least significant zero (to ensure the
    increase is not too large) that is more significant than a one (to ensure
    that the swap causes an increase).

    This ensures that the number is strictly greater than the input.
    To ensure that it is the next number the remaining (less-significant) bit
    must be sorted (unset bits more significant than set bits) to get the
    smallest possible number.
    """

    bin_string = f'0{prev:b}'
    i = bin_string.rfind("01")
    counts = Counter(bin_string[i + 2:])
    return int(f'{bin_string[:i]}10{"0" * counts["0"]}{"1" * counts["1"]}', 2)
