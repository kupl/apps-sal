# SOLUTION:
# Actually doing the reversals repeatedly is slow. Through observeration
# we can find a mapping of single shifts which take the original string directly
# to the target string while saving a lot of computation. The resulting "optimized"
# manipulations will be different for strings of different lengths,
# but the same for all strings of a given length.
#
# Over the course of multiple sets of reversals, each character necessarily goes through a loop.
# For example, if the original string is '1234', then the character at index 0
# will first move to index 1, then after another set of reversals to index 3,
# and then back to index 0, thus completing a loop.
# Index 2 may always stay in place.
# For longer strings, the mapping often results in having multiple of these loops.
#
# Once the loops are mapped out, we can easily determine where each character will end up
# after applying the reversal function x times.

def string_func(in_str, action_times):

    input_len = len(in_str)
    input_mid_point = (input_len + 1) / 2 - 1

    # First we'll map out the loops.
    # Starting from index 0, figure out where each character will go after one set of reversals.

    loops = [[0]]
    index = 0

    # Keep track of which loop each character starts in, so that when we want to place it in our new string we'll know where to look.
    # Right now they're all set to 0, but that will change as we check each index.
    loop_index_is_in = [0] * input_len

    indices_not_checked = list(range(1, input_len))

    while len(indices_not_checked) != 0:

        # Next-step transitions can be easily calculated
        if index < input_mid_point:
            index = index * 2 + 1
        elif index > input_mid_point:
            index = (input_len - 1 - index) * 2
        elif index == input_mid_point:
            index = input_len - 1

        # Next, we'll need to find each of the next locations (the "loop") for that character.

        # If we return to an index we've already checked, it means that we've completed a loop and we're done with that start index.
        # In that case, we'll add a new empty loop to loops and switch to checking an index that hasn't been checked yet,
        # until we've mapped out all of the loops.
        if index not in indices_not_checked:
            loops.append([])
            index = indices_not_checked[0]

        # Adding the index to the loop it belongs in (the loop we are building is always the last one in loops,
        # as any earlier loops we've already completed.)
        loops[-1].append(index)

        indices_not_checked.remove(index)

        # And we'll keep track of which loop each character starts in,
        # so that when we want to place it in our final result string we'll know where to look.
        loop_index_is_in[index] = len(loops) - 1

    # Now that we mapped out the loops, we need to find which index each character will end up at.

    # For now the final result string (new_string) is actually a list, so that we can use item assignment.
    new_string = [0] * input_len

    # For each character in the origional string:
    for char_index in range(input_len):

        # Find the loop that it is in:
        loop = loops[loop_index_is_in[char_index]]

        # Find where it is in that loop
        place_in_loop = loop.index(char_index)

        # Figure out where it will go (where it is in the loop, plus the amount of
        # times we want to apply the reversal function, which is the amount of 'steps' the character will take, mod the length of the loop)
        new_index = loop[(place_in_loop + action_times) % len(loop)]

        # Insert the character in its place in new_string
        new_string[new_index] = in_str[char_index]

    # After placing each character in the new_string list, convert the list to a string and return it. That's our final result string.
    return ''.join(new_string)
