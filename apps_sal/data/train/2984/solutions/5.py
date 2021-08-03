from math import ceil


def infected_zeroes(lst):
    # convert out list to a string for processing and split on "infected" zeroes
    chunks_of_ones = ''.join([str(l) for l in lst]).split('0')

    longest_chunk_of_ones = max([len(c) for c in chunks_of_ones])

    # if our longest run is the starting or ending chunk, num_turns is going to be the length of that chunk
    # however, all other chunks will be getting infected from both sides, so in those cases we divide by two
    num_turns = max(len(chunks_of_ones[0]), ceil(longest_chunk_of_ones / 2), len(chunks_of_ones[-1]))

    return num_turns
