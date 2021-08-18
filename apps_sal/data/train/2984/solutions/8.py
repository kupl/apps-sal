from re import sub
from math import ceil


def infected_zeroes(lst):
    chunks_of_ones = ''.join([str(l) for l in lst]).split('0')

    longest_chunk_of_ones = max([len(c) for c in chunks_of_ones])

    num_turns = max(len(chunks_of_ones[0]), ceil(longest_chunk_of_ones / 2), len(chunks_of_ones[-1]))

    return num_turns
